var getChinaMapOption=function () {
var geoCoordMap = {
    '新疆': [86.22, 44.30],
    '九江': [116.00, 29.70],
    '新乡': [116.402217, 35.311657],
    ' ':[79.92,37.12],
    '  ':[86.85,47.70],
    '若羌县':[88.17,39.02],
    '上海': [121.4648, 31.2891],
    '东莞': [113.8953, 22.901],
    '东营': [118.7073, 37.5513],
    '中山': [113.4229, 22.478],
    '临汾': [111.4783, 36.1615],
    '临沂': [118.3118, 35.2936],
    '丹东': [124.541, 40.4242],
    '丽水': [119.5642, 28.1854],
    '乌鲁木齐': [87.9236, 43.5883],
    '佛山': [112.8955, 23.1097],
    '保定': [115.0488, 39.0948],
    '兰州': [103.5901, 36.3043],
    '包头': [110.3467, 41.4899],
    '北京': [116.4551, 40.2539],
    '北海': [109.314, 21.6211],
    '南京': [118.8062, 31.9208],
    '南宁': [108.479, 23.1152],
    '南昌': [116.0046, 28.6633],
    '南通': [121.1023, 32.1625],
    '厦门': [118.1689, 24.6478],
    '台州': [121.1353, 28.6688],
    '合肥': [117.29, 32.0581],
    '呼和浩特': [111.4124, 40.4901],
    '咸阳': [108.4131, 34.8706],
    '哈尔滨': [127.9688, 45.368],
    '唐山': [118.4766, 39.6826],
    '嘉兴': [120.9155, 30.6354],
    '大同': [113.7854, 39.8035],
    '大连': [122.2229, 39.4409],
    '天津': [117.4219, 39.4189],
    '太原': [112.3352, 37.9413],
    '威海': [121.9482, 37.1393],
    '宁波': [121.5967, 29.6466],
    '宝鸡': [107.1826, 34.3433],
    '宿迁': [118.5535, 33.7775],
    '常州': [119.4543, 31.5582],
    '广州': [113.5107, 23.2196],
    '廊坊': [116.521, 39.0509],
    '延安': [109.1052, 36.4252],
    '张家口': [115.1477, 40.8527],
    '徐州': [117.5208, 34.3268],
    '德州': [116.6858, 37.2107],
    '惠州': [114.6204, 23.1647],
    '成都': [103.9526, 30.7617],
    '扬州': [119.4653, 32.8162],
    '承德': [117.5757, 41.4075],
    '拉萨': [91.1865, 30.1465],
    '无锡': [120.3442, 31.5527],
    '日照': [119.2786, 35.5023],
    '昆明': [102.9199, 25.4663],
    '杭州': [119.5313, 29.8773],
    '枣庄': [117.323, 34.8926],
    '柳州': [109.3799, 24.9774],
    '株洲': [113.5327, 27.0319],
    '武汉': [114.3896, 30.6628],
    '汕头': [117.1692, 23.3405],
    '江门': [112.6318, 22.1484],
    '沈阳': [123.1238, 42.1216],
    '沧州': [116.8286, 38.2104],
    '河源': [114.917, 23.9722],
    '泉州': [118.3228, 25.1147],
    '泰安': [117.0264, 36.0516],
    '泰州': [120.0586, 32.5525],
    '济南': [117.1582, 36.8701],
    '济宁': [116.8286, 35.3375],
    '海口': [110.3893, 19.8516],
    '淄博': [118.0371, 36.6064],
    '淮安': [118.927, 33.4039],
    '深圳': [114.5435, 22.5439],
    '清远': [112.9175, 24.3292],
    '温州': [120.498, 27.8119],
    '渭南': [109.7864, 35.0299],
    '湖州': [119.8608, 30.7782],
    '湘潭': [112.5439, 27.7075],
    '滨州': [117.8174, 37.4963],
    '潍坊': [119.0918, 36.524],
    '烟台': [120.7397, 37.5128],
    '玉溪': [101.9312, 23.8898],
    '珠海': [113.7305, 22.1155],
    '盐城': [120.2234, 33.5577],
    '盘锦': [121.9482, 41.0449],
    '石家庄': [114.4995, 38.1006],
    '福州': [119.4543, 25.9222],
    '秦皇岛': [119.2126, 40.0232],
    '绍兴': [120.564, 29.7565],
    '聊城': [115.9167, 36.4032],
    '肇庆': [112.1265, 23.5822],
    '舟山': [122.2559, 30.2234],
    '苏州': [120.6519, 31.3989],
    '莱芜': [117.6526, 36.2714],
    '菏泽': [115.6201, 35.2057],
    '营口': [122.4316, 40.4297],
    '葫芦岛': [120.1575, 40.578],
    '衡水': [115.8838, 37.7161],
    '衢州': [118.6853, 28.8666],
    '西宁': [101.4038, 36.8207],
    '西安': [109.1162, 34.2004],
    '贵阳': [106.6992, 26.7682],
    '连云港': [119.1248, 34.552],
    '邢台': [114.8071, 37.2821],
    '邯郸': [114.4775, 36.535],
    '郑州': [113.4668, 34.6234],
    '鄂尔多斯': [108.9734, 39.2487],
    '重庆': [107.7539, 30.1904],
    '金华': [120.0037, 29.1028],
    '铜川': [109.0393, 35.1947],
    '银川': [106.3586, 38.1775],
    '镇江': [119.4763, 31.9702],
    '长春': [125.8154, 44.2584],
    '长沙': [113.0823, 28.2568],
    '长治': [112.8625, 36.4746],
    '阳泉': [113.4778, 38.0951],
    '青岛': [120.4651, 36.3373],
    '韶关': [113.7964, 24.7028]
};

var BJData = [
    [{
        name: '新乡'
    }, {
        name: '新乡',
        value: 200
    }],
    [{
        name: '新乡'
    }, {
        name: '呼和浩特',
        value: 90
    }],
     [{
        name: '新乡'
    }, {
        name: '哈尔滨',
        value: 90
    }],
    [{
        name: '新乡'
    }, {
        name: '石家庄',
        value: 90
    }],
    [{
        name: '新乡'
    }, {
        name: '昆明',
        value: 30
    }],
    [{
        name: '新乡'
    }, {
        name: '北京',
        value: 100
    }],
    [{
        name: '新乡'
    }, {
        name: '长春',
        value: 40
    }],
     [{
        name: '新乡'
    }, {
        name: '重庆',
        value: 40
    }],
    [{
        name: '新乡'
    }, {
        name: '贵阳',
        value: 50
    }],
    [{
        name: '新乡'
    }, {
        name: '南宁',
        value: 30
    }],
    [{
        name: '新乡'
    }, {
        name: '济南',
        value: 10
    }],
    [{
        name: '新乡'
    }, {
        name: '太原',
        value: 40
    }],
    [{
        name: '新乡'
    }, {
        name: '西安',
        value: 60
    }],
    [{
        name: '新乡'
    }, {
        name: '武汉',
        value: 50
    }],
    [{
        name: '新乡'
    }, {
        name: '合肥',
        value: 40
    }],
    [{
        name: '新乡'
    }, {
        name: '南京',
        value: 30
    }],
    [{
        name: '新乡'
    }, {
        name: '沈阳',
        value: 20
    }],
    [{
        name: '新乡'
    }, {
        name: '成都',
        value: 10
    }]
];

var SHData = [
     [{
        name: '九江'
    }, {
        name: '九江',
        value: 200
    }],

    [{
        name: '九江'
    }, {
        name: '长沙',
        value: 95
    }],
    [{
        name: '九江'
    }, {
        name: '武汉',
        value: 30
    }],
    [{
        name: '九江'
    }, {
        name: '南昌',
        value: 20
    }],
    [{
        name: '九江'
    }, {
        name: '合肥',
        value: 70
    }],
    [{
        name: '九江'
    }, {
        name: '南京',
        value: 60
    }],
    [{
        name: '九江'
    }, {
        name: '福州',
        value: 50
    }],
    [{
        name: '九江'
    }, {
        name: '上海',
        value: 100
    }],
    [{
        name: '九江'
    }, {
        name: '深圳',
        value: 100
    }],

];

var GZData = [
    [{
        name: '新疆'
    }, {
        name: '新疆',
        value: 200
    }],
    [{
        name: '新疆'
    }, {
        name: '  ',
        value: 90
    }],
    [{
        name: '新疆'
    }, {
        name: ' ',
        value: 40
    }],
    [{
        name: '新疆'
    }, {
        name: '呼和浩特',
        value: 90
    }],
    [{
        name: '新疆'
    }, {
        name: '昆明',
        value: 40
    }],
    [{
        name: '新疆'
    }, {
        name: '成都',
        value: 10
    }],
    [{
        name: '新疆'
    }, {
        name: '兰州',
        value: 95
    }],
    [{
        name: '新疆'
    }, {
        name: '银川',
        value: 90
    }],
    [{
        name: '新疆'
    }, {
        name: '西宁',
        value: 80
    }],

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
    ['新乡', BJData],
    ['九江', SHData],
    ['新疆', GZData]
].forEach(function(item, i) {
    series.push({
        name: item[0] + ' Top10',
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
        name: item[0] + ' Top10',
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
        name: item[0] + ' Top10',
        type: 'effectScatter',
        coordinateSystem: 'geo',
        zlevel: 2,
        rippleEffect: {
            brushType: 'stroke'
        },
        label: {
            normal: {
                show: false,        // 名称显示
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
    title: {
        // text: '模拟迁徙',
        // subtext: '数据纯属虚构',
        left: 'left',
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
        label: {
            emphasis: {
                show: false
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


// var getChinaMapOption=function (){
//     var geoCoordMap = {
//     '上海': [121.4648, 31.2891],
//     '武汉': [114.3896, 30.6628],
//     '安徽': [117.29, 32.0581],
//     '北京': [116.4551, 40.2539],
//     '大连': [122.2229, 39.4409],
//     '福建': [119.4543, 25.9222],
//     '甘肃': [103.5901, 36.3043],
//     '广西': [108.479, 23.1152],
//     '广州': [113.5107, 23.2196],
//     '贵州': [106.6992, 26.7682],
//     '海南': [110.3893, 19.8516],
//     '河北': [114.4995, 38.1006],
//     '河南': [113.4668, 34.6234],
//     '黑龙江': [127.9688, 45.368],
//     '湖北': [114.3896, 30.6628],
//     '湖南': [113.0823, 28.2568],
//     '吉林': [125.8154, 44.2584],
//     '江苏': [118.8062, 31.9208],
//     '江西': [116.0046, 28.6633],
//     '辽宁': [123.1238, 42.1216],
//     '内蒙': [111.4124, 40.4901],
//     '宁波': [121.5967, 29.6466],
//     '宁夏': [106.3586, 38.1775],
//     '青岛': [120.4651, 36.3373],
//     '青海': [101.4038, 36.8207],
//     '山东': [117.1582, 36.8701],
//     '山西': [112.3352, 37.9413],
//     '陕西': [109.1162, 34.2004],
//     '深圳': [114.5435, 22.5439],
//     '四川': [103.9526, 30.7617],
//     '天津': [117.4219, 39.4189],
//     '西藏': [91.1865, 30.1465],
//     '厦门': [118.1689, 24.6478],
//     '新疆': [87.9236, 43.5883],
//     '云南': [102.9199, 25.4663],
//     '浙江': [119.5313, 29.8773],
//     '重庆': [107.7539, 30.1904]
// };
//
// var ERData = [
//     [{name: '新疆'}, {name: '上海',value: 178725}],
//     [{name: '云南'}, {name: '上海',value: 266633}],
//     [{name: '内蒙'}, {name: '武汉',value: 436902}],
//     [{name: '海南'}, {name: '武汉',value: 217414}]
// ];
//
// var SHData = [
//     [{name: '上海'}, {name: '上海',value: 483629}],
//     [{name: '安徽'}, {name: '上海',value: 563822}],
//     [{name: '北京'}, {name: '上海',value: 1221703}],
//     [{name: '大连'}, {name: '上海',value: 218584}],
//     [{name: '福建'}, {name: '上海',value: 555425}],
//     [{name: '甘肃'}, {name: '上海',value: 168855}],
//     [{name: '广西'}, {name: '上海',value: 436735}],
//     [{name: '广州'}, {name: '上海',value: 691167}],
//     [{name: '贵州'}, {name: '上海',value: 184743}],
//     [{name: '海南'}, {name: '上海',value: 180274}],
//     [{name: '河北'}, {name: '上海',value: 462582}],
//     [{name: '河南'}, {name: '上海',value: 1074537}],
//     [{name: '黑龙江'}, {name: '上海',value: 229617}],
//     [{name: '湖北'}, {name: '上海',value: 942161}],
//     [{name: '湖南'}, {name: '上海',value: 2377490}],
//     [{name: '吉林'}, {name: '上海',value: 217103}],
//     [{name: '江苏'}, {name: '上海',value: 1890847}],
//     [{name: '江西'}, {name: '上海',value: 268140}],
//     [{name: '辽宁'}, {name: '上海',value: 511873}],
//     [{name: '内蒙'}, {name: '上海',value: 287642}],
//     [{name: '宁波'}, {name: '上海',value: 253987}],
//     [{name: '宁夏'}, {name: '上海',value: 63600}],
//     [{name: '青岛'}, {name: '上海',value: 253564}],
//     [{name: '青海'}, {name: '上海',value: 30286}],
//     [{name: '山东'}, {name: '上海',value: 1608024}],
//     [{name: '山西'}, {name: '上海',value: 426826}],
//     [{name: '陕西'}, {name: '上海',value: 478508}],
//     [{name: '深圳'}, {name: '上海',value: 516034}],
//     [{name: '四川'}, {name: '上海',value: 403750}],
//     [{name: '天津'}, {name: '上海',value: 264792}],
//     [{name: '西藏'}, {name: '上海',value: 24723}],
//     [{name: '厦门'}, {name: '上海',value: 854658}],
//     [{name: '浙江'}, {name: '上海',value: 436902}],
//     [{name: '重庆'}, {name: '上海',value: 217414}]
// ];
//
// var WHData = [
//     [{name: '上海'}, {name: '武汉',value: 483629}],
//     [{name: '安徽'}, {name: '武汉',value: 563822}],
//     [{name: '北京'}, {name: '武汉',value: 1221703}],
//     [{name: '大连'}, {name: '武汉',value: 218584}],
//     [{name: '福建'}, {name: '武汉',value: 555425}],
//     [{name: '甘肃'}, {name: '武汉',value: 168855}],
//     [{name: '广西'}, {name: '武汉',value: 436735}],
//     [{name: '广州'}, {name: '武汉',value: 691167}],
//     [{name: '贵州'}, {name: '武汉',value: 184743}],
//     [{name: '河北'}, {name: '武汉',value: 462582}],
//     [{name: '河南'}, {name: '武汉',value: 1074537}],
//     [{name: '黑龙江'}, {name: '武汉',value: 229617}],
//     [{name: '湖北'}, {name: '武汉',value: 942161}],
//     [{name: '湖南'}, {name: '武汉',value: 2377490}],
//     [{name: '吉林'}, {name: '武汉',value: 217103}],
//     [{name: '江苏'}, {name: '武汉',value: 1890847}],
//     [{name: '江西'}, {name: '武汉',value: 268140}],
//     [{name: '辽宁'}, {name: '武汉',value: 511873}],
//     [{name: '宁波'}, {name: '武汉',value: 253987}],
//     [{name: '宁夏'}, {name: '武汉',value: 63600}],
//     [{name: '青岛'}, {name: '武汉',value: 253564}],
//     [{name: '青海'}, {name: '武汉',value: 30286}],
//     [{name: '山东'}, {name: '武汉',value: 1608024}],
//     [{name: '山西'}, {name: '武汉',value: 426826}],
//     [{name: '陕西'}, {name: '武汉',value: 478508}],
//     [{name: '深圳'}, {name: '武汉',value: 516034}],
//     [{name: '四川'}, {name: '武汉',value: 403750}],
//     [{name: '天津'}, {name: '武汉',value: 264792}],
//     [{name: '西藏'}, {name: '武汉',value: 24723}],
//     [{name: '厦门'}, {name: '武汉',value: 854658}],
//     [{name: '新疆'}, {name: '武汉',value: 178725}],
//     [{name: '云南'}, {name: '武汉',value: 266633}],
//     [{name: '浙江'}, {name: '武汉',value: 436902}],
//     [{name: '重庆'}, {name: '武汉',value: 217414}]
// ];
//
//
// var convertData = function(data) {
//     console.log(data);
//     var res = [];
//     for (var i = 0; i < data.length; i++) {
//         var dataItem = data[i];
//         var fromCoord = geoCoordMap[dataItem[0].name];
//         var toCoord = geoCoordMap[dataItem[1].name];
//         if (fromCoord && toCoord) {
//             res.push({
//                 fromName: dataItem[0].name,
//                 toName: dataItem[1].name,
//                 coords: [fromCoord, toCoord],
//                 value: dataItem[1].value
//             });
//         }
//     }
//     return res;
// };
//
// var color = ['#E81010','#2FF9FF', '#a6c84c', ];
// var series = [];
// [
//     ['异常', ERData],
//     ['上海', SHData],
//     ['武汉', WHData]
// ].forEach(function(item, i) {
//     console.log(item, i);
//     series.push(
//         //    {
//         //    name: item[0],
//         //    type: 'lines',
//         //    zlevel: 1,
//         //    effect: {
//         //        show: true,
//         //        period: 6,
//         //        trailLength: 0.2,
//         //        color: '#fff',
//         //        symbolSize: 1
//         //    },
//         //    lineStyle: {
//         //        normal: {
//         //            color: color[i],
//         //            width: 0,
//         //            curveness: 0.2
//         //        }
//         //    },
//         //    data: convertData(item[1])},
//         {
//             name: item[0],
//             type: 'lines',
//             zlevel: 2,
//             symbol: ['none', 'arrow'],
//             symbolSize: 1,
//             effect: {
//                 show: true,
//                 constantSpeed: 30,
//                 symbol: 'pin',
//                 symbolSize: 3,
//                 trailLength: 0,
//             },
//             lineStyle: {
//                 normal: {
//                     color: color[i],
//                     width: 1,
//                     opacity: 0.6,
//                     curveness: 0.2
//                 }
//             },
//             data: convertData(item[1])
//         }, {
//             name: item[0],
//             type: 'effectScatter',
//             coordinateSystem: 'geo',
//             zlevel: 2,
//             rippleEffect: {
//                 brushType: 'stroke'
//             },
//             label: {
//                 normal: {
//                     show: true,
//                     position: 'right',
//                     formatter: '{b}'
//                 }
//             },
//             symbolSize: function(val) {
//                 return val[2] / 8;
//             },
//             itemStyle: {
//                 normal: {
//                     color: color[i]
//                 }
//             },
//             data: item[1].map(function(dataItem) {
//                 return {
//                     name: dataItem[0].name,
//                     value: geoCoordMap[dataItem[0].name].concat([dataItem[0].value])
//                 };
//             })
//         });
// });
// console.log(series)
//
// option = {
//    // backgroundColor: '#404a59',
//     title: {
//         text: '全国交易分布',
//        // subtext: '公网入口',
//         left: 'center',
//         top:100,
//         textStyle: {
//             color: '#fff'
//
//         }
//     },
//     tooltip: {
//         trigger: 'item',
//         formatter: function(params, ticket, callback) {
//             console.log(params);
//             if (params.seriesType == "effectScatter") {
//                 return "线路：" + params.data.name + "" + params.data.value[2];
//             } else if (params.seriesType == "lines") {
//                 return params.data.fromName + ">" + params.data.toName + "<br />" + params.data.value;
//             } else {
//                 return params.name;
//             }
//         }
//     },
//     legend: {
//         orient: 'vertical',
//         x:490,
//         y:650,
//         data: ['异常','上海', '武汉'],
//         textStyle: {
//             color: '#fff'
//         },
//         selectedMode: 'multiple',
//     },
//     geo: {
//         map: 'china',
//         label: {
//             emphasis: {
//                 show: true,
//                 color: '#fff'
//             }
//         },
//         roam: true,
//         itemStyle: {
//             normal: {
//                // areaColor: '#323c48',
//                // borderColor: '#404a59'
//                  areaColor: '#091E57',
//                  borderColor: '#6DA5C2',
//                    // borderColor:'rgb(87,170,198)',
//                  borderWidth:1
//             },
//             emphasis: {
//                 areaColor: '#2a333d'
//             }
//         }
//     },
//     series: series
// };
//     return option;
//     }



