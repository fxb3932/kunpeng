var getRight_2Option=function(data){
// his_tot=(297290/10000).toFixed(2)
// cur_tot=(220779/10000).toFixed(2)
//
// his_amt=(1570003548/10000).toFixed(2)
// cur_amt=(146578217/10000).toFixed(2)
// his_tot=1000
// cur_tot=930
// his_amt=1999
// cur_amt=1111

his_tot=(data.his_tot/10000).toFixed(2)
cur_tot=(data.cur_tot/10000).toFixed(2)
his_amt=((data.his_amt)/10000).toFixed(2)
cur_amt=(data.cur_amt/10000).toFixed(2)
//苏宁银行:1461129657


visits=[]
visits[0]=(cur_tot/his_tot*100).toFixed(2)
visits[1]=(cur_amt/his_amt*100).toFixed(2)


if((cur_tot/his_tot*100) > 100)
{
    aaa=1
}
else
{
    aaa=visits[0]/100
}

if((cur_amt/his_amt*100) >100 )
{
    bbb=1
}
else
{
    bbb=visits[1]/100
}


//cost[交易量占比，交易额占比]
// var cost = [1, 0.801]//本期比上期（大于1按1处理）
// aaa=1
// bbb=0.2
cost = [aaa,bbb]//本期比上期（大于1按1处理）
//dataCost[交易量,交易额]
var dataCost = [cur_tot,cur_amt]//真是的金额

var totalCost = [1, 1]//比例综合
// var visits = [91, 102]//本期占总的百分比*100
var grade = ['交易量:', '交易额:']
var data = {

    grade: grade,
    cost: cost,
    totalCost: totalCost,
    visits: visits,
    dataCost:dataCost
};
option = {
    // backgroundColor: '#05274C',
    title: {
        top: '5%',
        left: 'left',
        text: '历史同期比对',
        textStyle: {
            align: 'center',
            color: '#fff',
            // fontSize: 18
        }
    },
          title: {
        text: '历史同期比对',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    tooltip:{

    },
    grid: {
        left: '180',
        right: '200'
    },
    xAxis: {
        show: false,
    },
    yAxis: {
        type: 'category',
        axisLabel: {
            margin: 110,
            show: true,
            color: '#4DCEF8',
            fontSize: 18,
            // align:'botto'
        },
        axisTick: {
            show: false,
        },
        axisLine: {
            show: false,
        },
        data: data.grade
    },
    series: [
        {
        type: 'bar',
        barGap: '-100%',
        label: {
            normal: {
                show: true,
                position: 'right',
                color: '#fff',
                fontSize: 16,
                formatter:
                function(param) {
                    if(param.dataIndex=='0'){
                    return '历史量:'+his_tot+'万\n'+'同比：'+data.visits[param.dataIndex] +'%';
                    }
                    if(param.dataIndex=='1'){
                       return '历史金额:'+his_amt+'万\n'+'同比：'+data.visits[param.dataIndex]  +'%';
                    }

                },
            }
        },
        // barWidth: '35%',
             barWidth: '65%',
        itemStyle: {
            normal: {
                borderColor: '#4DCEF8',
                borderWidth: 2,
                barBorderRadius: 15,
                color: 'rgba(102, 102, 102,0)'
            },
        },
        z: 1,
        data: data.totalCost,
        // data: da
    }, {
        type: 'bar',
        barGap: '-98%',
        // barWidth: '33%',
            barWidth: '63%',
        itemStyle: {
            normal: {
                barBorderRadius: 16,
                color: {
                    type: 'linear',
                    x: 0,
                    x1: 1,
                    colorStops: [{
                        offset: 0,
                        color: '#02ddff'
                    }, {
                        offset: 1,
                        color: '#00feff'
                    }]
                }
            },
        },
        max: 1,
        label: {
            normal: {
                show: true,
                position: 'left',
                color: '#fff',
                fontSize: 16,
                formatter: function(param) {
                    if(param.dataIndex=='0'){
                        return data.dataCost[param.dataIndex] + '(万)';
                    }
                    if(param.dataIndex=='1'){
                       return data.dataCost[param.dataIndex] + '(万)';
                    }

                },
            }
        },
        labelLine: {
            show: true,
        },
        z: 2,
        data: data.cost,
    }]
}
return option;
}