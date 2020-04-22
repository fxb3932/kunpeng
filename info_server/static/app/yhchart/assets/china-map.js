var getChinaMapOption=function () {
var geoCoordMap = {
    '上海': [121.4648, 31.2891],
    '邯郸': [114.47, 36.6],
    '库尔勒': [86.06, 41.68],
    '达州':[107.509,31.221],
    '哈密':[93.44,42.78],
    '雅安':[103.065,30.03],
    '南阳':[112.52,33.00],
    '临朐聚丰':[118.53,36.5],
    '中山小榄':[113.38,22.52],
    '大洼恒丰':[122.07,41.12],
    '梅州客商':[116.1,24.55],
    '费县梁邹':[117.97,35.26],


    '安徽': [117.29, 32.0581],
    '大连': [122.2229, 39.4409],
    '甘肃': [103.5901, 36.3043],
    '广西': [108.479, 23.1152],
    '广州': [113.5107, 23.2196],
    '贵州': [106.6992, 26.7682],
    '海南': [110.3893, 19.8516],
    '河北': [114.4995, 38.1006],
    '河南': [113.4668, 34.6234],
    '黑龙江': [127.9688, 45.368],
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
    '新疆': [87.9236, 43.5883],
    '云南': [102.9199, 25.4663],
    '浙江': [119.5313, 29.8773],


};
    var BJData = [
        [{name: '邯郸'}, {name: '邯郸', value: 150}],
        [{name: '库尔勒'}, {name: '库尔勒', value: 100}],
        [{name: '达州'}, {name: '达州', value: 80}],
        [{name: '哈密'}, {name: '哈密', value: 1}],
        [{name: '雅安'}, {name: '雅安', value: 1}],
        [{name: '南阳'}, {name: '南阳', value: 1}],
        [{name: '临朐聚丰'}, {name: '临朐聚丰', value: 1}],
        [{name: '中山小榄'}, {name: '中山小榄', value: 1}],
        [{name: '大洼恒丰'}, {name: '大洼恒丰', value: 1}],
        [{name: '梅州客商'}, {name: '梅州客商', value: 1}],
        [{name: '费县梁邹'}, {name: '费县梁邹', value: 1}],



    ]

var SHData = [
    [{name: '上海'}, {name: '上海',value: 250}],
    [{name: '安徽'}, {name: '上海',value: 0}],
    [{name: '大连'}, {name: '上海',value: 0}],
    [{name: '甘肃'}, {name: '上海',value: 0}],
    [{name: '广西'}, {name: '上海',value: 0}],
    [{name: '广州'}, {name: '上海',value: 0}],
    [{name: '贵州'}, {name: '上海',value: 0}],
    [{name: '海南'}, {name: '上海',value: 0}],
    [{name: '河北'}, {name: '上海',value: 0}],
    [{name: '河南'}, {name: '上海',value: 0}],
    [{name: '黑龙江'}, {name: '上海',value: 0}],
    [{name: '吉林'}, {name: '上海',value: 0}],
    [{name: '江苏'}, {name: '上海',value: 0}],
    [{name: '江西'}, {name: '上海',value: 0}],
    [{name: '辽宁'}, {name: '上海',value: 0}],
    [{name: '内蒙'}, {name: '上海',value: 0}],
    [{name: '宁波'}, {name: '上海',value: 0}],
    [{name: '宁夏'}, {name: '上海',value: 0}],
    [{name: '青岛'}, {name: '上海',value: 0}],
    [{name: '青海'}, {name: '上海',value: 0}],
    [{name: '山东'}, {name: '上海',value: 0}],
    [{name: '山西'}, {name: '上海',value: 0}],
    [{name: '陕西'}, {name: '上海',value: 0}],
    [{name: '深圳'}, {name: '上海',value: 0}],
    [{name: '四川'}, {name: '上海',value: 0}],
    [{name: '天津'}, {name: '上海',value: 0}],
    [{name: '浙江'}, {name: '上海',value: 0}],


];

var GZData = [
    [{name: '邯郸'}, {name: '上海', value: 0}],
    [{name: '库尔勒'}, {name: '上海', value: 0}],
    [{name: '达州'}, {name: '上海', value: 0}],
    [{name: '哈密'}, {name: '上海', value: 0}],
    [{name: '雅安'}, {name: '上海', value: 0}],
    [{name: '南阳'}, {name: '上海', value: 0}],
    [{name: '临朐聚丰'}, {name: '上海', value: 0}],
    [{name: '中山小榄'}, {name: '上海', value: 0}],
    [{name: '大洼恒丰'}, {name: '上海', value: 0}],
    [{name: '梅州客商'}, {name: '上海', value: 0}],
    [{name: '费县梁邹'}, {name: '上海', value: 0}],




];

var planePath = 'path://M.6,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705';

var convertData = function(data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var dataItem = data[i];
        var fromCoord = geoCoordMap[dataItem[0].name];
        var toCoord = geoCoordMap[dataItem[1].name];
        if (fromCoord && toCoord) {
            res.push([{
                coord: fromCoord
            }, {
                coord: toCoord
            }]);
        }
    }
    return res;
};

var color = ['#3ed4ff', '#ffa022', '#a6c84c'];
var series = [];
[
    ['', BJData],
    ['上海', SHData],
    ['', GZData]
].forEach(function(item, i) {
    series.push({
        // name: item[0] + ' Top10',
        type: 'lines',
        zlevel: 1,
        // 流动线
        effect: {
            show: true,
            period: 6,
            trailLength: 0.7,
            color: '#fff',
            symbolSize: 3
        },
        lineStyle: {
            normal: {
                color: color[i],
                width: 0,
                curveness: 0.2
            }
        },
        data: convertData(item[1])
    }, {    //实线
        // name: item[0] + ' Top10',
        type: 'lines',
        zlevel: 2,
        effect: {
            show: true,
            period: 6,
            trailLength: 0,
            symbol: planePath,
            symbolSize: 15
        },
        lineStyle: {
            normal: {
                color: color[i],
                width: 1,
                opacity: 0.4,
                curveness: 0.2
            }
        },
        data: convertData(item[1])
    }, {
        // name: item[0] + ' Top10',
        type: 'effectScatter',
        coordinateSystem: 'geo',
        zlevel: 2,
        rippleEffect: {
            brushType: 'stroke'
        },
        label: {
            normal: {
                show: true,        // 名称显示
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
                name: dataItem[1].name,
                value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value])
            };
        })
    });
});

option = {
    // backgroundColor: '#080a20',
    // title: {
    //     text: 'TOP交易地区分布',
    //     // subtext: '数据纯属虚构',
    //     left: 'center',
    //     textStyle: {
    //         color: '#fff'
    //     }
    // },
        title: {
        text: '合作行交易分布',
       // subtext: '公网入口',
        left: 'center',
        top:60,
        textStyle: {
            color: '#fff'

        }
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        top: 'bottom',
        left: 'right',
        data: ['北京 Top10', '上海 Top10', '广州 Top10'],
        textStyle: {
            color: '#fff'
        },
        selectedMode: 'single'
    },
    geo: {
        map: 'china',
        zoom:1.25,
        label: {
            emphasis: {
                show: true,
                color:'#fff'
            }
        },
        roam: true,
        itemStyle: {
            normal: {
                areaColor: '#132937',
                borderColor: '#0692a4'
            },
            emphasis: {
                areaColor: '#0b1c2d'
            }
        }
    },
    series: series
};
return option;
}





