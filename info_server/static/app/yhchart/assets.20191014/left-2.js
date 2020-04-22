var getLeft_2Option=function(){

option = {
   // backgroundColor: '#0E2A43',
   title: {
        text: '商踪密南北交易量',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    legend: {
         align: 'right',
        top:40,
        right: 10,
        textStyle: {
            color: "#fff"
        },
        itemWidth: 10,
        itemHeight: 10,
        itemGap: 10,
        data: ['南方', '北方']
    },
     grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    
     tooltip: {
        show:"true",
        trigger: 'axis',
        axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    xAxis:  {
        type: 'value',
        axisTick : {show: false},
        axisLine: {
            show: false,
            lineStyle:{
                color:'#fff',
            }
        },
        splitLine: {
            show: false
        },
    },
    yAxis: [
            {
                type: 'category',
                axisTick : {show: false},
                axisLine: {
                    show: true,
                    lineStyle:{
                        color:'#fff',
                    }
                },
                data: ["16:00","16:01","16:02","16:03","16:04","16:05","16:06","16:07","16:08","16:09"]
            },
            {
                type: 'category',
                axisLine: {show:false},
                axisTick: {show:false},
                axisLabel: {show:false},
                splitArea: {show:false},
                splitLine: {show:false},
                data: ["16:00","16:01","16:02","16:03","16:04","16:05","16:06","16:07","16:08","16:09"]
            },
            
    ],
    series: [
        {
            name: '南方',
            type: 'bar',
            yAxisIndex:1,
            
            itemStyle:{
                normal: {
                    show: true,
                    color: '#277ace',
                    barBorderRadius:50,
                    borderWidth:0,
                    borderColor:'#333',
                }
            },
            barGap:'0%',
            barCategoryGap:'50%',
            data: [120, 132, 101, 134, 90, 230, 210, 125, 231, 132]
        },
        {
            name: '北方',
            type: 'bar',
            itemStyle:{
                normal: {
                    show: true,
                    color: '#5de3e1',
                    barBorderRadius:50,
                    borderWidth:0,
                    borderColor:'#333',
                }
            },
            barGap:'0%',
            barCategoryGap:'50%',
            data: [32, 52, 41, 64, 15, 10, 32, 25, 210, 32]
        }
       
    ]
};
return option;

}