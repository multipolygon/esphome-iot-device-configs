#include <map>

// Home Assistant weather icons for Android or ESPHome
// https://www.home-assistant.io/integrations/weather/

std::map<std::string, std::string> weather_icon_map
  {
    // official:
    {"clear-night", "\U000F0594"},
    {"cloudy", "\U000F0590"},
    {"fog", "\U000F0591"},
    {"hail", "\U000F0592"},
    {"lightning", "\U000F0593"},
    {"lightning-rainy", "\U000F067E"},
    {"partlycloudy", "\U000F0595"},
    {"pouring", "\U000F0596"},
    {"rainy", "\U000F0597"},
    {"snowy", "\U000F0598"},
    {"snowy-rainy", "\U000F067F"},
    {"sunny", "\U000F0599"},
    {"windy", "\U000F059D"},
    {"windy-variant", "\U000F059E"},
    {"exceptional", "\U000F0026"},
    // other:
    {"cloudy-alert", "\U000F0F2F"},
    {"cloudy-arrow-right", "\U000F0E6E"},
    {"hazy", "\U000F0F30"},
    {"hurricane", "\U000F0898"},
    {"night", "\U000F0594"},
    {"night-partly-cloudy", "\U000F0F31"},
    {"partly-lightning", "\U000F0F32"},
    {"partly-rainy", "\U000F0F33"},
    {"partly-snowy", "\U000F0F34"},
    {"partly-snowy-rainy", "\U000F0F35"},
    {"snowy-heavy", "\U000F0F36"},
    {"sunny-alert", "\U000F0F37"},
    {"sunny-off", "\U000F14E4"},
    {"sunset", "\U000F059A"},
    {"sunset-down", "\U000F059B"},
    {"sunset-up", "\U000F059C"},
    {"tornado", "\U000F0F38"},
  };
