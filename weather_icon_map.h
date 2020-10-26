#include <map>

// https://www.home-assistant.io/integrations/weather/
std::map<std::string, std::string> weather_icon_map
  {
   {"clear-night",     "\U000F0594"}, // night
   {"cloudy",          "\U000F0590"},
   {"fog",             "\U000F0591"},
   {"hail",            "\U000F0592"},
   {"lightning",       "\U000F0593"},
   {"lightning-rainy", "\U000F067E"},
   {"partlycloudy",    "\U000F0595"},
   {"pouring",         "\U000F0596"},
   {"rainy",           "\U000F0597"},
   {"snowy",           "\U000F0598"},
   {"snowy-rainy",     "\U000F0F35"},
   {"sunny",           "\U000F0599"},
   {"windy",           "\U000F059D"},
   {"windy-variant",   "\U000F059E"},
   {"exceptional",     "\U000F0898"}, // hurricane
  };
