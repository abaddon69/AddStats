import uiScriptLocale

window = {
	"name" : "RefineDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 220,
	"height" : 120,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 220,
			"height" : 120,
			"title" : uiScriptLocale.ADD_STATS,
			"children" :
			(
				{
					"name" : "StatsSlot",
					"type" : "slotbar",

					"x" : 20,
					"y" : 35,

					"width" : 180,
					"height" : 20,

					#"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "StatsValue",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"text" : "",

							"all_align" : "center",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "slider",
					"type" : "sliderbar",

					"x" : 0,
					"y" : 66,

					"horizontal_align" : "center",
				},
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : -35,
					"y" : 35,

					"text" : uiScriptLocale.ADD,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 35,
					"y" : 35,

					"text" : uiScriptLocale.CANCEL,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
				},
			),
		},
	),
}