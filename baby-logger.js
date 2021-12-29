import fs from "fs";
import yaml from "yaml";
import _ from "lodash";

const TARGET_FILE = "baby-logger.yaml";

const structure = {
  state: ["AWAKE", "SLEEPING", "FEEDING", "WALK", "BATH", "CAR", "TUMMY_TIME"],
  nappy: ["CLEAN", "PEE", "POO"],
};

const specialActions = {};

const stateSwitches = []
  .concat(
    ...Object.entries(structure).map(([mode, states]) =>
      states.map((state, i) =>
        yaml.createNode({
          platform: "template",
          id: `${state.toLowerCase()}_${mode}_mode_switch`,
          name: `Baby ${_.startCase(state.toLowerCase())}`,
          icon: `mdi:$${state}_MDI`,
          restore_state: false,
          retain: false,
          lambda: `return id(${mode}) == ${i + 1};`,
          turn_on_action: [
            { lambda: `id(${mode}) = ${i + 1};` },
            ...(specialActions?.[mode]?.[state] || []),
          ],
          turn_off_action: {
            if: {
              condition: { lambda: `return id(${mode}) == ${i + 1};` },
              then: [
                { lambda: `id(${mode}) = 0;` },
                { delay: "500ms" },
                { lambda: `id(${mode}) = ${i + 1};` },
                ...(specialActions?.[mode]?.[state] || []),
              ],
            },
          },
        })
      )
    )
  )
  .map((x) => {
    x.commentBefore = " Auto generated:";
    return x;
  });

const textSensorLambdas = _.mapValues(structure, (states, mode) =>
  `
switch (id(${mode})) {
${states.map((state, i) => `case ${i + 1}: return {"$${state}"};`).join("\n")}
default: return {""};
}
`.trim()
);

console.log(textSensorLambdas);

const config = yaml.parseDocument(fs.readFileSync(TARGET_FILE, "utf8"));

if (config.get("switch") === null) {
  config.set("switch", stateSwitches);
} else {
  config.set("switch", [
    ...config
      .get("switch")
      .items.filter((x) => !/_mode_switch$/.test(x.get("id"))),
    ...stateSwitches,
  ]);
}

Object.entries(textSensorLambdas).forEach(([mode, lambda]) =>
  config
    .get(`text_sensor`)
    .items.find((x) => x.get("id") == `${mode}_text`)
    .set("lambda", lambda)
);

fs.writeFileSync(TARGET_FILE, config.toString(), "utf8");
