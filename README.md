# RTL Podcast URL

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/christophebaraer/rtl_podcastURL?include_prereleases&style=flat-square)

The RTL Podcast URL provides a new sensor with the URL to the last full-length episode of the "Grosses Têtes" show.

Go to [Github](https://github.com/christophebaraer/rtl_podcastURL) for Pre-requisites and Setup Instructions.


## How to use / Installation

### Automaticly using HACS (Home Assistant Community Store)

1. Go into HACS in the left menu
2. Add a "Custom repositories" (on the top right hand corner)
3. Add "https://github.com/christophebaraer/rtl_podcastURL" in the field and select category "Integrations"
4. Click + (Explore and add repository) - Blue button in bottom right
6. Search for "rtl_podcastURL"
7. [Update configuration.yaml](#update-configuration)


### Or manually
To get started with this superexperimental implementation:

1. Clone or download the project to [HA config path]/custom_components/rtl_podcastURL:
2. Go to directory - `cd [HA config path]/custom_components/rtl_podcastURL`
3. Move files - `mv custom_components/* .`
4. [Update configuration.yaml](#update-configuration)


### Update configuration
* Add the following to your Home Assistant configuration file:

      # RTL Podcast URL
        - platform: rtl_podcastURL


* Restart Home Assistant
