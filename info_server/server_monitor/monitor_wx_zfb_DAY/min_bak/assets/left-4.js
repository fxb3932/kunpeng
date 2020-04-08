var getLeft_4Option=function(){
 var option = {
     title: {
        text: '公网入口交易耗时笔数',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        },
        
    },

   // backgroundColor: '#fff',
    color: ['#16c2af', '#ffc751', '#4162ff', '#ff6e72', '#9692ff'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        align: 'right',
        top:35,
        right: 10,
        textStyle: {
            color: "#fff"
        },
        itemWidth: 10,
        itemHeight: 10,
        itemGap: 5,
        data: ['0-2秒', '2-5秒', '5-10秒', '>10秒']
        
    },
     grid: {
        top:'60',
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    yAxis: [{
        type: 'value',
        splitLine: {
            show: true,
            lineStyle: {
                color: ['#fff']
            }
        },
        axisLine: {
            show: false,
            lineStyle: {
                color: "#00c7ff",
                width: 1,
                type: "solid"
            },
        }
    }],
    xAxis: [{
        type: 'category',
        axisLabel: {
            show: true,
            textStyle: {
                color: "#00c7ff",
            }
        },
        data: ['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']
    }],
    series: [{
            name: '0-2秒',
            type: 'bar',
            barWidth: 5,
            stack: '交易耗时',
            data: [620, 732, 701, 734, 1090, 1130, 1120, 2341, 2322, 4331, 4422]
        },
        {
            name: '2-5秒',
            type: 'bar',
            stack: '交易耗时',
            data: [120, 132, 101, 134, 290, 230, 220, 123, 332, 441, 1522]
        },
        {
            name: '5-10秒',
            type: 'bar',
            stack: '交易耗时',
            data: [60, 72, 71, 74, 190, 130, 110, 142, 160, 322, 310]
        },
        {
            name: '>10秒',
            type: 'bar',
            stack: '交易耗时',
            data: [62, 82, 91, 84, 109, 110, 120, 80, 41, 103, 221]
        }
    ]
};
 
return option;
}