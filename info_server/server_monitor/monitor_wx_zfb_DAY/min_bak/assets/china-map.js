
var getChinaMapOption=function (){
    var geoCoordMap = {
    '上海': [121.4648, 31.2891],
    '武汉': [114.3896, 30.6628],
    '安徽': [117.29, 32.0581],
    '北京': [116.4551, 40.2539],
    '大连': [122.2229, 39.4409],
    '福建': [119.4543, 25.9222],
    '甘肃': [103.5901, 36.3043],
    '广西': [108.479, 23.1152],
    '广州': [113.5107, 23.2196],
    '贵州': [106.6992, 26.7682],
    '海南': [110.3893, 19.8516],
    '河北': [114.4995, 38.1006],
    '河南': [113.4668, 34.6234],
    '黑龙江': [127.9688, 45.368],
    '湖北': [114.3896, 30.6628],
    '湖南': [113.0823, 28.2568],
    '吉林': [125.8154, 44.2584],
    '江苏': [118.8062, 31.9208],
    '江西': [116.0046, 28.6633],
    '辽宁': [123.1238, 42.1216],
    '内蒙': [111.4124, 40.4901],
    '宁波': [121.5967, 29.6466],
    '宁夏': [106.3586, 38.1775],
    '青岛': [120.4651, 36.3373],
    '青海': [101.4038, 36.8207],
    '山东': [117.1582, 36.8701],
    '山西': [112.3352, 37.9413],
    '陕西': [109.1162, 34.2004],
    '深圳': [114.5435, 22.5439],
    '四川': [103.9526, 30.7617],
    '天津': [117.4219, 39.4189],
    '西藏': [91.1865, 30.1465],
    '厦门': [118.1689, 24.6478],
    '新疆': [87.9236, 43.5883],
    '云南': [102.9199, 25.4663],
    '浙江': [119.5313, 29.8773],
    '重庆': [107.7539, 30.1904]
};

var ERData = [
    [{name: '新疆'}, {name: '上海',value: 178725}],
    [{name: '云南'}, {name: '上海',value: 266633}],
    [{name: '内蒙'}, {name: '武汉',value: 436902}],
    [{name: '海南'}, {name: '武汉',value: 217414}]
];

var SHData = [
    [{name: '上海'}, {name: '上海',value: 483629}],
    [{name: '安徽'}, {name: '上海',value: 563822}],
    [{name: '北京'}, {name: '上海',value: 1221703}],
    [{name: '大连'}, {name: '上海',value: 218584}],
    [{name: '福建'}, {name: '上海',value: 555425}],
    [{name: '甘肃'}, {name: '上海',value: 168855}],
    [{name: '广西'}, {name: '上海',value: 436735}],
    [{name: '广州'}, {name: '上海',value: 691167}],
    [{name: '贵州'}, {name: '上海',value: 184743}],
    [{name: '海南'}, {name: '上海',value: 180274}],
    [{name: '河北'}, {name: '上海',value: 462582}],
    [{name: '河南'}, {name: '上海',value: 1074537}],
    [{name: '黑龙江'}, {name: '上海',value: 229617}],
    [{name: '湖北'}, {name: '上海',value: 942161}],
    [{name: '湖南'}, {name: '上海',value: 2377490}],
    [{name: '吉林'}, {name: '上海',value: 217103}],
    [{name: '江苏'}, {name: '上海',value: 1890847}],
    [{name: '江西'}, {name: '上海',value: 268140}],
    [{name: '辽宁'}, {name: '上海',value: 511873}],
    [{name: '内蒙'}, {name: '上海',value: 287642}],
    [{name: '宁波'}, {name: '上海',value: 253987}],
    [{name: '宁夏'}, {name: '上海',value: 63600}],
    [{name: '青岛'}, {name: '上海',value: 253564}],
    [{name: '青海'}, {name: '上海',value: 30286}],
    [{name: '山东'}, {name: '上海',value: 1608024}],
    [{name: '山西'}, {name: '上海',value: 426826}],
    [{name: '陕西'}, {name: '上海',value: 478508}],
    [{name: '深圳'}, {name: '上海',value: 516034}],
    [{name: '四川'}, {name: '上海',value: 403750}],
    [{name: '天津'}, {name: '上海',value: 264792}],
    [{name: '西藏'}, {name: '上海',value: 24723}],
    [{name: '厦门'}, {name: '上海',value: 854658}],
    [{name: '浙江'}, {name: '上海',value: 436902}],
    [{name: '重庆'}, {name: '上海',value: 217414}]
];

var WHData = [
    [{name: '上海'}, {name: '武汉',value: 483629}],
    [{name: '安徽'}, {name: '武汉',value: 563822}],
    [{name: '北京'}, {name: '武汉',value: 1221703}],
    [{name: '大连'}, {name: '武汉',value: 218584}],
    [{name: '福建'}, {name: '武汉',value: 555425}],
    [{name: '甘肃'}, {name: '武汉',value: 168855}],
    [{name: '广西'}, {name: '武汉',value: 436735}],
    [{name: '广州'}, {name: '武汉',value: 691167}],
    [{name: '贵州'}, {name: '武汉',value: 184743}],
    [{name: '河北'}, {name: '武汉',value: 462582}],
    [{name: '河南'}, {name: '武汉',value: 1074537}],
    [{name: '黑龙江'}, {name: '武汉',value: 229617}],
    [{name: '湖北'}, {name: '武汉',value: 942161}],
    [{name: '湖南'}, {name: '武汉',value: 2377490}],
    [{name: '吉林'}, {name: '武汉',value: 217103}],
    [{name: '江苏'}, {name: '武汉',value: 1890847}],
    [{name: '江西'}, {name: '武汉',value: 268140}],
    [{name: '辽宁'}, {name: '武汉',value: 511873}],
    [{name: '宁波'}, {name: '武汉',value: 253987}],
    [{name: '宁夏'}, {name: '武汉',value: 63600}],
    [{name: '青岛'}, {name: '武汉',value: 253564}],
    [{name: '青海'}, {name: '武汉',value: 30286}],
    [{name: '山东'}, {name: '武汉',value: 1608024}],
    [{name: '山西'}, {name: '武汉',value: 426826}],
    [{name: '陕西'}, {name: '武汉',value: 478508}],
    [{name: '深圳'}, {name: '武汉',value: 516034}],
    [{name: '四川'}, {name: '武汉',value: 403750}],
    [{name: '天津'}, {name: '武汉',value: 264792}],
    [{name: '西藏'}, {name: '武汉',value: 24723}],
    [{name: '厦门'}, {name: '武汉',value: 854658}],
    [{name: '新疆'}, {name: '武汉',value: 178725}],
    [{name: '云南'}, {name: '武汉',value: 266633}],
    [{name: '浙江'}, {name: '武汉',value: 436902}],
    [{name: '重庆'}, {name: '武汉',value: 217414}]
];


var convertData = function(data) {
    console.log(data);
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var dataItem = data[i];
        var fromCoord = geoCoordMap[dataItem[0].name];
        var toCoord = geoCoordMap[dataItem[1].name];
        if (fromCoord && toCoord) {
            res.push({
                fromName: dataItem[0].name,
                toName: dataItem[1].name,
                coords: [fromCoord, toCoord],
                value: dataItem[1].value
            });
        }
    }
    return res;
};

var color = ['#E81010','#2FF9FF', '#a6c84c', ];
var series = [];
[
    ['异常', ERData],
    ['上海', SHData],
    ['武汉', WHData]
].forEach(function(item, i) {
    console.log(item, i);
    series.push(
        //    {
        //    name: item[0],
        //    type: 'lines',
        //    zlevel: 1,
        //    effect: {
        //        show: true,
        //        period: 6,
        //        trailLength: 0.2,
        //        color: '#fff',
        //        symbolSize: 1
        //    },
        //    lineStyle: {
        //        normal: {
        //            color: color[i],
        //            width: 0,
        //            curveness: 0.2
        //        }
        //    },
        //    data: convertData(item[1])}, 
        {
            name: item[0],
            type: 'lines',
            zlevel: 2,
            symbol: ['none', 'arrow'],
            symbolSize: 1,
            effect: {
                show: true,
                constantSpeed: 30,
                symbol: 'pin',
                symbolSize: 3,
                trailLength: 0,
            },
            lineStyle: {
                normal: {
                    color: color[i],
                    width: 1,
                    opacity: 0.6,
                    curveness: 0.2
                }
            },
            data: convertData(item[1])
        }, {
            name: item[0],
            type: 'effectScatter',
            coordinateSystem: 'geo',
            zlevel: 2,
            rippleEffect: {
                brushType: 'stroke'
            },
            label: {
                normal: {
                    show: true,
                    position: 'right',
                    formatter: '{b}'
                }
            },
            symbolSize: function(val) {
                return val[2] / 8;
            },
            itemStyle: {
                normal: {
                    color: color[i]
                }
            },
            data: item[1].map(function(dataItem) {
                return {
                    name: dataItem[0].name,
                    value: geoCoordMap[dataItem[0].name].concat([dataItem[0].value])
                };
            })
        });
});
console.log(series)

option = {
   // backgroundColor: '#404a59',
    title: {
        text: '全国交易分布',
       // subtext: '公网入口',
        left: 'center',
        top:20,
        textStyle: {
            color: '#fff'
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: function(params, ticket, callback) {
            console.log(params);
            if (params.seriesType == "effectScatter") {
                return "线路：" + params.data.name + "" + params.data.value[2];
            } else if (params.seriesType == "lines") {
                return params.data.fromName + ">" + params.data.toName + "<br />" + params.data.value;
            } else {
                return params.name;
            }
        }
    },
    legend: {
        orient: 'vertical',
        x:490,
        y:650,
        data: ['异常','上海', '武汉'],
        textStyle: {
            color: '#fff'
        },
        selectedMode: 'multiple',
    },
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: true,
                color: '#fff'
            }
        },
        roam: true,
        itemStyle: {
            normal: {
               // areaColor: '#323c48',
               // borderColor: '#404a59'
                 areaColor: '#091E57',
                 borderColor: '#6DA5C2',
                   // borderColor:'rgb(87,170,198)',
                 borderWidth:1
            },
            emphasis: {
                areaColor: '#2a333d'
            }
        }
    },
    series: series
};
    return option;
    }



