<div id='{{ id }}' style="width:800px; height:600px;"></div>
<script>
    require.config({
         paths:{
            echarts: 'http://echarts.baidu.com/gallery/vendors/echarts/echarts-all-3',
            dataTool: 'http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min',
            china: 'http://echarts.baidu.com/gallery/vendors/echarts/map/js/china',
            world: 'http://echarts.baidu.com/gallery/vendors/echarts/map/js/world',
            bmap: 'http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min',
         }
    });

    require(['echarts', 'dataTool', 'china', 'world', 'bmap'],function(echarts){
                var myChart = echarts.init(document.getElementById('{{ id }}'));
                var option;
                {{ globaljsobj }}
                option = {{ opt }};
                myChart.setOption(option);
    });
</script>
