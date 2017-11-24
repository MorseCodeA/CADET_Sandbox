$(document).ready(function(){
            $("#open_btn").click(function() {
            $.FileDialog({multiple: true}).on('files.bs.filedialog', function(ev) {
                var files = ev.files;
                var text = "";
                files.forEach(function(f) {
                    text += f.name + "<br/>";
                });
                $("#output").html(text);
            }).on('cancel.bs.filedialog', function(ev) {
                $("#output").html("Cancelled!");
            });
        });
  //Deals with uploader
  uuid = $('#progressBar').data('progress_bar_uuid');

  // form submission
  $('form').submit(function(){
    // Prevent multiple submits
    if ($.data(this, 'submitted')) return false;
    // Append X-Progress-ID uuid form action
    this.action += (this.action.indexOf('?') == -1 ? '?' : '&') + 'X-Progress-ID=' + uuid;
    // Update progress bar
    function update_progress_info() {
      $.getJSON(upload_progress_url, {'X-Progress-ID': uuid}, function(data, status){
          var progress = parseInt(data.received, 10)/parseInt(data.size, 10)*100;
          $('#progressBar').attr('value', progress);
        window.setTimeout(update_progress_info, 200);
      });
    }
    window.setTimeout(update_progress_info, 200);
    $.data(this, 'submitted', true); // mark form as submitted.
    return true;
  });
});
