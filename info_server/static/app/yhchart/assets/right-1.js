
var getRight_1Option=function(data){
    var colors = ['#66CDAA', '#B8860B', '#FF9080'];
    var data_hd = [421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632, 421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632, 421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632, 421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632]
    var data_xy = [121, 256, 119, 258, 358, 343, 220, 216, 151, 221, 266, 532, 421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632, 421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632, 421, 356, 719, 658, 458, 443, 620, 416, 551, 721, 466, 632]
    var data_rate = [99, 98, 95, 92, 91, 90, 85, 82, 81, 80, 78, 97, 99, 98, 95, 92, 91, 90, 85, 82, 81, 80, 78, 97, 99, 98, 95, 92, 91, 90, 85, 82, 81, 80, 78, 97, 99, 98, 95, 92, 91, 90, 85, 82, 81, 80, 78, 97]

data_time=data.time_list;
data_hd=data.hdwl_list;
data_xy=data.xywl_list;
data_rate=data.rate_list;

// var xData = function() {
//     var data = [];
//     for (var i = 1; i < 52; i++) {
//         data.push("地区"+i);
//     }
//     return data;
// }();
option = {
     // backgroundColor: "#113A71",
          title: {
        text: '平台交易成功率',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    // title: {
    //     text: '地区办理情况',
    //       left:'45%',
    //       top:'10%',
    //     textStyle:{
    //          fontSize: '15' ,
    //          color: "#fff"
    //     }
    // },
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {
            "type": "shadow",
            textStyle: {
                color: "#fff"
            }

        },
    },
   grid: {
        top:'30%',
        bottom:'10%',
        left:'10%',
        right:'10%',
    },
    legend: {
        data:['邯郸网联','兴业网联','成功率'],
        align: 'right',
         top:'10%',
         right:'5%',
        textStyle:{
            color:'#FFFFFF'
        }

    },
     "calculable": true,
    // "xAxis": [
    //     {
    //     "type": "category",
    //     "axisLine": {
    //         lineStyle: {
    //             color: '#000'
    //         }
    //     },
    //     "splitLine": {
    //         "show": false
    //     },
    //     "axisTick": {
    //         "show": false
    //     },
    //     "splitArea": {
    //         "show": false
    //     },
    //     "axisLabel": {
    //         "interval": 0,
    //         textStyle:{
    //             fontSize:10,
    //             color: '#ffffff'
    //         }
    //     },
    //         // data: xData,
    //         data: data_time
    // }
    // ],
    xAxis: [

        {
        nameLocation:'middle',
            nameRotate:15,
            type: 'category',

            axisTick: {
                alignWithLabel: true
            },
             axisLabel: {
            show: true,
            textStyle: {
                color: "#00c7ff",
            }
        },
            data: data_time
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '',
            // min: 0,
            // max: 2000,
            position: 'left',
            axisLine: {
                lineStyle: {
                    color: '#ffffff'
                }
            },
            axisLabel: {
                formatter: '{value} '
            },

            splitLine:{
                show:false
            }
        },
        {
            type: 'value',

            name: '',
            position: 'right',
            axisLine: {
                lineStyle: {
                    color: '#ffffff'
                }
            },
            axisLabel: {
                formatter: '{value} %'
            },
              splitLine:{
                show:false
            }
        }
    ],
    series: [
        {"name": "邯郸网联",
            "type": "bar",
            "stack": "总量",
            "barMaxWidth": 15,
            "barGap": "10%",
            "itemStyle": {
                "normal": {
                   "color": "#06a7ef",
                    "label": {
                        "show": false,
                        "textStyle": {
                            "color": "#fff"
                        },
                        "position": "insideTop",
                        formatter: function(p) {
                            return p.value > 0 ? (p.value) : '';
                        }
                    }
                }
            },
            data:data_hd
        },
        {"name": "兴业网联",
            "type": "bar",
            "stack": "总量",
            "itemStyle": {
                "normal": {
                     "color": "#d872f3",
                    "barBorderRadius": 0,
                    "label": {
                        "show": false,
                        "position": "top",
                        formatter: function(p) {
                            return p.value > 0 ? (p.value) : '';
                        }
                    }

                /*normal:{
                color:new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#00b0ff'
                }, {
                    offset: 0.8,
                    color: '#7052f4'
                }], false)}*/
            }
            },
            data:data_xy
        },
        {
        name:'成功率',
        yAxisIndex: 1,
        symbolSize:6,
        symbol:'circle',
        type:'line',
        "itemStyle": {
            "normal": {
                "color": "rgba(252,230,48,1)",
                "barBorderRadius": 0,
                "label": {
                    "show": false,
                    "position": "top",
                    formatter: function(p) {
                        return p.value > 0 ? (p.value/100) : '';
                    }
                }
            }
        },
        data:data_rate
    }]
};

return option;
}