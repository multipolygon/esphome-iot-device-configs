import fs from "fs";
import yaml from "yaml";
import _ from "lodash";

const stateSwitches = []
  .concat(
    ...Object.entries({
      state: ["AWAKE", "SLEEPING", "FEEDING", "WALK", "BATH"],
      nappy: ["DRY", "WET", "DIRTY"],
    }).map(([mode, states]) =>
      states.map((state) =>
        yaml.createNode({
          platform: "template",
          id: `${state.toLowerCase()}_${mode}_mode_switch`,
          name:
            mode === "state"
              ? `Baby ${_.startCase(state.toLowerCase())}`
              : `${_.startCase(state.toLowerCase())} Nappy`,
          icon: `mdi:$${state}_MDI`,
          restore_state: true,
          lambda: `return id(${mode}).state == "$${state}";`,
          turn_on_action: {
            "text_sensor.template.publish": { id: mode, state: `$${state}` },
          },
          turn_off_action: [
            { "text_sensor.template.publish": { id: mode, state: `$BLANK` } },
            { delay: "500ms" },
            {
              "text_sensor.template.publish": { id: mode, state: `$${state}` },
            },
          ],
        })
      )
    )
  )
  .map((x) => {
    x.commentBefore = " Auto generated:";
    return x;
  });

const config = yaml.parseDocument(fs.readFileSync("baby_logger.yaml", "utf8"));

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

fs.writeFileSync("baby_logger.yaml", config.toString(), "utf8");
