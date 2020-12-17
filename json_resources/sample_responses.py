all_lights = {
                "1": {
                        "state": {
                            "on": False,
                            "bri": 1,
                            "hue": 33761,
                            "sat": 254,
                            "effect": "none",
                            "xy": [
                                0.3171,
                                0.3366
                            ],
                            "ct": 159,
                            "alert": "none",
                            "colormode": "xy",
                            "mode": "homeautomation",
                            "reachable": True
                        },
                        "swupdate": {
                            "state": "noupdates",
                            "lastinstall": "2018-01-02T19:24:20"
                        },
                        "type": "Extended color light",
                        "name": "Hue color lamp 7",
                        "modelid": "LCT007",
                        "manufacturername": "Philips",
                        "productname": "Hue color lamp",
                        "capabilities": {
                            "certified": True,
                            "control": {
                                "mindimlevel": 5000,
                                "maxlumen": 600,
                                "colorgamuttype": "B",
                                "colorgamut": [
                                    [
                                        0.675,
                                        0.322
                                    ],
                                    [
                                        0.409,
                                        0.518
                                    ],
                                    [
                                        0.167,
                                        0.04
                                    ]
                                ],
                                "ct": {
                                    "min": 153,
                                    "max": 500
                                }
                            },
                            "streaming": {
                                "renderer": True,
                                "proxy": False
                            }
                        },
                        "config": {
                            "archetype": "sultanbulb",
                            "function": "mixed",
                            "direction": "omnidirectional"
                        },
                        "uniqueid": "00:17:88:01:00:bd:c7:b9-0b",
                        "swversion": "5.105.0.21169"
                    }
                }

test_light = {
                "state": {
                    "hue": 50000,
                    "on": True,
                    "effect": "none",
                    "alert": "none",
                    "bri": 200,
                    "sat": 200,
                    "ct": 500,
                    "xy": [0.5, 0.5],
                    "reachable": True,
                    "colormode": "hs"
                },
                "type": "Living Colors",
                "name": "LC 1",
                "modelid": "LC0015",
                "swversion": "1.0.3"
                }

all_groups = {
            "1": {
                "name": "Group 1",
                "lights": [
                    "1",
                    "2"
                ],
                "type": "LightGroup",
                "action": {
                    "on": True,
                    "bri": 254,
                    "hue": 10000,
                    "sat": 254,
                    "effect": "none",
                    "xy": [
                        0.5,
                        0.5
                    ],
                    "ct": 250,
                    "alert": "select",
                    "colormode": "ct"
                }
            },
            "2": {
                "name": "Group 2",
                "lights": [
                    "3",
                    "4",
                    "5"
                ],
                "type": "LightGroup",
                "action": {
                    "on": True,
                    "bri": 153,
                    "hue": 4345,
                    "sat": 254,
                    "effect": "none",
                    "xy": [
                        0.5,
                        0.5
                    ],
                    "ct": 250,
                    "alert": "select",
                    "colormode": "ct"
                }
            }
        }

test_group = {
                "action": {
                    "on": True,
                    "hue": 0,
                    "effect": "none",
                    "bri": 100,
                    "sat": 100,
                    "ct": 500,
                    "xy": [0.5, 0.5]
                },
                "lights": [
                    "1",
                    "2"
                ],
                "state":{
                    "any_on":True, 
                    "all_on":True
                },   
                "type":"Room",   
                "class":"Bedroom",   
                "name":"Master bedroom"
            }

actions = ["on", "bri", "hue", "sat", "xy", "ct" "alert", "effect", "transitiontime", "bri_inc", "sat_inc", "hue_inc", "ct_inc", "xy_inc", "scene"]

group_keys = ["name", "lights", "class"]