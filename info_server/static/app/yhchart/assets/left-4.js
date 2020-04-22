var getLeft_4Option=function(settle_date,data_wx,data_zfb,data_other){
    settle_date=settle_date
    data_wx=data_wx
    data_zfb=data_zfb
    data_other=data_other



    // settle_date=[400, 500, 500, 500, 500, 400,400, 500, 500]
    // data_wx=[400, 500, 500, 500, 500, 400,400, 500, 500]
    // data_zfb=[400, 500, 500, 500, 500, 400,400, 500, 500]
    // data_other=[400, 500, 500, 500, 500, 400,400, 500, 500]
   var option = {
     // backgroundColor:'#323a5e',
          title: {
        text: '代理网联交易类型分布',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          left: '2%',
          right: '4%',
          bottom: '14%',
          top:'16%',
          containLabel: true
        },
         legend: {
        data: ['微信', '支付宝', '总量'],
        right: 10,
        top:12,
        textStyle: {
            color: "#fff"
        },
        itemWidth: 12,
        itemHeight: 10,
        // itemGap: 35
    },
        xAxis: {
          type: 'category',
          data: settle_date,
          axisLine: {
            lineStyle: {
              color: 'white'

            }
          },
          axisLabel: {
            // interval: 0,
            // rotate: 40,
            textStyle: {
              fontFamily: 'Microsoft YaHei'
            }
          },
        },

        yAxis: {
          type: 'value',
          // max:'1200',
          axisLine: {
            show: false,
            lineStyle: {
              color: 'white'
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              color: 'rgba(255,255,255,0.3)'
            }
          },
          axisLabel: {}
        },
        // "dataZoom": [
        //     {
        //   "show": true,
        //   "height": 12,
        //   "xAxisIndex": [
        //     0
        //   ],
        //   bottom:'8%',
        //   "start": 10,
        //   "end": 100,
        //   handleSize: '110%',
        //   handleStyle:{
        //     color:"#d3dee5",
        //
        //   },
        //   textStyle:{
        //     color:"#fff"},
        //   borderColor:"#90979c"
        // }, {
        //   "type": "inside",
        //   "show": true,
        //   "height": 15,
        //   "start": 1,
        //   "end": 35
        // }],
        series: [{
          name: '微信',
          type: 'bar',
          barWidth: '15%',
          itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#fccb05'
                }, {
                    offset: 1,
                    color: '#f5804d'
                }]),
                barBorderRadius: 12,
            },
          },
          data: data_wx
        },
        {
          name: '支付宝',
          type: 'bar',
          barWidth: '15%',
          itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#8bd46e'
                }, {
                    offset: 1,
                    color: '#09bcb7'
                }]),
                barBorderRadius: 11,
            }

          },
          data: data_zfb
        },
        {
          name: '总量',
          type: 'bar',
          barWidth: '15%',
          itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#248ff7'
                }, {
                    offset: 1,
                    color: '#6851f1'
                }]),
            barBorderRadius: 11,
            }
          },
          data: data_other
        }]
      };




return option;
}