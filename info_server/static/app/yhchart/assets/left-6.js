var getLeft_6Option=function(){
var data_val=[2220, 1682, 2791, 3000, 4090, 3230, 2910,2220, 1682, 2791, 3000, 4090],
    xAxis_val=['2:00','4:00','6:00', '8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00', '24:00'];
var option = {
   // backgroundColor:'#293042',
    grid:{
        left:10,
        top:'25%',
        bottom:10,
        right:10,
        containLabel:true
    },
    tooltip:{
        show:true,
        backgroundColor:'#384157',
        borderColor:'#384157',
        borderWidth:1,
        formatter:'{b}:{c}',
        extraCssText:'box-shadow: 0 0 5px rgba(0, 0, 0, 1)'
    },
    /*
    legend:{
        right:0,
        top:0,
        data:['距离'],
         textStyle:{
            color :'#5c6076'
        }
    },
    */
    title: {
        text: '核心系统交易趋势',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    xAxis: {
       
        data: xAxis_val,
        boundaryGap:false,
        axisLine:{
            show:false
        },
         splitLine:{show:false},
         axisLabel: {
            show:true,
            textStyle: {
                color: '#008cff'
            }  
        },
        axisTick:{
            show:false
        }
    },
    yAxis: { 
        ayisLine:{
            show:false
        },
         axisLabel: {
            show:true,
            textStyle: {
                color: '#008cff'
            }  
        },
        splitLine:{
            show:false,
            lineStyle:{
                color:'#2e3547'
            }
        },
                
        axisLine: {show:false
                //lineStyle: { color: '#384157'}
            }
            
          
    },
    
    series: [
      
        {
            type: 'line',
            name:'linedemo',
            smooth:true,
            symbolSize:10,
            animation:false,
            lineWidth:1.2,
            hoverAnimation:false,
            data:data_val,
            symbol:'circle',
            itemStyle:{
                normal:{
                    color:'#008cff',
                    //shadowBlur: 40,
                    label:{
                        show:false,
                        position:'top',
                        textStyle:{
                            color:'#008cff',
                    
                        }
                    }
                }
            },
           areaStyle:{
                normal:{
                    color:'#f17a52',
                    opacity:0.08
                }
            }
            
        }
    ]
};

return option;
}