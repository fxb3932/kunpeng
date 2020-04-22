
var getRight_1Option=function(){
 
var  xData=['2:00','4:00','6:00', '8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00', '24:00'];
var yDate=[327,1776,507,1200,800,482,204,1390,1001,951,381,220];
var option = {
    //backgroundColor: "#344b58",
    "title": {
        "text": "当日受理交易量",
       // "subtext": "BY Wang Dingding",
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        },
        subtextStyle: {
            color: '#90979c',
            fontSize: '16',
            x:50,
            y:10

        },
    },
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
        left: '3%',
        right: '4%',
        bottom: '5%',
        containLabel: true
    },


    "calculable": true,
    "xAxis": [{
        "type": "category",
        "axisLine": {
            lineStyle: {
                color: '#90979c'
            }
        },
        "splitLine": {
            "show": false
        },
        "axisTick": {
            "show": false
        },
        "splitArea": {
            "show": false
        },
        "axisLabel": {
            "interval": 0,

        },
        "data": xData,
    }],
    "yAxis": [{
        "type": "value",
        "splitLine": {
            "show": false
        },
        "axisLine": {
            lineStyle: {
                color: '#90979c'
            }
        },
        "axisTick": {
            "show": false
        },
        "axisLabel": {
            "interval": 0,

        },
        "splitArea": {
            "show": false
        },

    }],
 
    "series": [

        {
            "name": "交易量",
            "type": "bar",
            "stack": "交易量",
            "barMaxWidth": 15,
            "barGap": "10%",
            "itemStyle": {
                "normal": {
                    "color": "rgba(0,191,183,1)",
                    "barBorderRadius": 0,
                    "label": {
                        "show": false,
                        "position": "top"
                    }
                }
            },
            "data": yDate
        }, {
            "name": "交易量",
            "type": "line",
            "stack": "交易量",
            symbolSize:10,
            symbol:'circle',
            "itemStyle": {
                "normal": {
                    "color": "rgba(252,230,48,1)",
                    "barBorderRadius": 0,
                    "label": {
                        "show": false,
                        "position": "top",
                        
                    }
                }
            },
           "data": yDate
        },
    ]
}
return option;
}