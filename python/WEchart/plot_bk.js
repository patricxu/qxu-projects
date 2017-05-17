<div id='{{ id }}' style="width:800px; height:600px;"></div>
<script>
    require.config({
         paths:{
            echarts: '//cdn.bootcss.com/echarts/3.2.3/echarts.min',
            //echarts: './echarts.min.js',
         }
    });

    require(['echarts'],function(echarts){
                var myChart = echarts.init(document.getElementById('{{ id }}'));
                {{ globaljsobj }}
                var option = {{ opt }};
                myChart.setOption(option);
    });
</script>

