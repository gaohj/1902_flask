$(function () {
   var ue = UE.getEditor('container', {
         'serverUrl':'/ueditor/upload/'
    });

   $("#submitBtn").click(function (event) {
        event.preventDefault();
        var titleInput = $('input[name="title"]');
        var boardSelect = $('select[name="board_id"]');
        var title = titleInput.val();
        var board_id = boardSelect.val();
        var content = ue.getContent();

        ajax_1902.post({
            'url':'/apost/',
            'data':{
                'title':title,
                'board_id':board_id,
                'content':content
            },
            'success':function (data) {
                if(data['code'] == 200){

                }else {

                }
            }
        })
   })

})