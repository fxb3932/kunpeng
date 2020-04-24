var getRight_3Option=function(data) {

    // trans_tot='12344'
    // wx_rate=60
    // zfb_rate=35
    // other_rate=5
    //

    trans_tot=data.wx_data +data.zfb_data +data.other_data
    wx_rate=(data.wx_data/trans_tot)*100
    wx_rate=wx_rate.toFixed(1)
    zfb_rate=(data.zfb_data/trans_tot)*100
    zfb_rate=zfb_rate.toFixed(1)
    other_rate=100 - wx_rate - zfb_rate
    other_rate=other_rate.toFixed(1)



option = {

    tooltip: {
        trigger: 'item',
        formatter: "{b} : {d}% <br/> {c}"
    },

       title: [
           {
               text: '渠道交易占比',
        x: 'left',
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16}
           },{
        text: trans_tot,
        subtext: '交易总量',
        x: 'center',
        y: '43%',
        textStyle: {
            fontSize: 20,
            fontWeight: 'normal',
            color: '#00FFFF',
        },
        subtextStyle: {
            fontSize: 15,
            fontWeight: 'normal',
            align:"center",
            color:'#CCCCCC'
        },
    }],
    series: [{
        type: 'pie',
        radius: ['65', '85'],
        center: ['50%', '50%'],
        color: [ '#00FFFF', '#FFA800','#4658F6'],
        itemStyle:{
     normal: {
        borderWidth: 2,
        borderColor: '#031845',
      }
},
        data: [
             {
                value: zfb_rate,
                name: '支付宝'
            },{
                value: wx_rate,
                name: '微信'
            },

            // {
            //     value: other_rate,
            //     name: '其他'
            // }

        ],
        labelLine: {
            normal: {
                show: true,
                length: 5,
                length2: 5,
                lineStyle: {

                    width: 1
                }
            }
        },
        label: {
            normal: {
                formatter: '{b|{b}}\n{hr|}\n{c|{c}%}',
                rich: {
                    b: {
                        fontSize: 15,
                        color: '#fff',
                        // align: 'left',
                        padding: 4
                    },
                    hr: {
                        // borderColor: '#CCCCCC',
                        // width: '100%',
                        borderWidth: 2,
                        height: 0
                    },
                    c: {
                        fontSize: 15,
                        align: 'center',
                        padding: 4,
                        color:'#00EDED'
                    }
                }
            }
        }
    }

    ]
};

return option
}

// var getRight_3Option=function(){
//     var dataStyle = {
//     normal: {
//         label: {
//             show: true,
//             color: '#fff',
//             fontSize: 12,
//         },
//         labelLine: {
//             //smooth: 0.2,
//             //指示线长
//             length: 20,
//             length2: 20
//         },
//     }
// };
//
// var labelShow = {
//     show: true,
//     color: '#fff',
//     fontSize: 15,
//     formatter: [
//         '{d| {d}% }',
//         '{b| {b} }'
//     ].join('\n'),
//     rich: {
//         d: {
//             fontSize: 15,
//             color: '#fff'
//         },
//         b: {
//             fontSize: 18,
//             color: '#fff'
//         },
//     }
// };
//
// var placeHolderStyle = {
//     normal: {
//         color: 'rgba(0,0,0,0)',
//         label: {
//             show: false
//         },
//         labelLine: {
//             show: false
//         }
//     },
//     emphasis: {
//         color: 'rgba(0,0,0,0)'
//     }
// };
// option = {
//     // backgroundColor: '#044061',
//
//     color: ['#2078d1', '#8a00ec', '#ff941b', '#fb0065'],
//     tooltip: {
//         show: true,
//         formatter: "{b} <br/> {c} ({d}%)"
//     },
//     angleAxis: {
//         type: 'category',
//         z: 10,
//         axisLine: {
//             color: '#fff',
//             lineStyle: {
//                 width: 3,
//                 color: '#fff',
//             }
//         },
//     },
//     radiusAxis: {
//         axisTick: {
//             show: false
//         },
//         axisLabel: {
//             show: false,
//             color: '#fff'
//         },
//         axisLine: {
//             show: false,
//             color: '#fff',
//             lineStyle: {
//                 color: '#fff',
//             }
//         },
//         splitLine: {
//             color: '#000',
//             lineStyle: {
//                 type: 'dotted',
//                 color: 'rgba(170,170,170,.5)',
//             }
//         },
//
//     },
//     polar: {
//         center: ['50%', '50%'],
//         radius: 70,
//     },
//     series: [
//         {
//             name: 'Line 1',
//             type: 'pie',
//             clockWise: false,
//             radius: [50, 62],
//             itemStyle: dataStyle,
//             hoverAnimation: false,
//             data: [{
//                     value: 260,
//                     name: '',
//                     itemStyle: placeHolderStyle
//                 },
//                 {
//                     value: 100,
//                     name: '微信',
//                     label: labelShow,
//                 },
//                 {
//                     value: 100,
//                     name: '',
//                     itemStyle: placeHolderStyle
//                 }
//
//             ]
//         },
//         {
//             name: 'Line 2',
//             type: 'pie',
//             clockWise: false,
//             radius: [35, 45],
//             itemStyle: dataStyle,
//             hoverAnimation: false,
//
//             data: [{
//                     value: 260,
//                     name: '',
//                     itemStyle: placeHolderStyle
//                 },
//                 {
//                     value: 130,
//                     name: '支付宝',
//                     label: labelShow,
//                 },
//                 {
//                     value: 130,
//                     name: '',
//                     itemStyle: placeHolderStyle
//                 }
//             ]
//         },
//         {
//             name: 'Line 3',
//             type: 'pie',
//             clockWise: false,
//             hoverAnimation: false,
//             radius: [25, 34],
//             itemStyle: dataStyle,
//
//             data: [{
//                     value: 260,
//                     name: '',
//                     itemStyle: placeHolderStyle
//                 },
//                 {
//                     value: 30,
//                     name: '其他',
//                     label: labelShow,
//                 },
//                 {
//                     value: 30,
//                     name: '',
//                     itemStyle: placeHolderStyle
//                 }
//             ]
//         },
//
//
//         {
//             type: 'bar',
//             data: [0],
//             coordinateSystem: 'polar',
//             name: '06a',
//             stack: 'a'
//         },
//
//     ]
// };
//
// return option;
// }