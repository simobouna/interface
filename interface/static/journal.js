var devices = JSON.parse(document.getElementById('devices').textContent);
select = document.getElementById('select')

var i;
for (i = 0; i < devices.length; i++) {
    option = document.createElement('option');
    option.setAttribute("value", devices[i]);
    option.textContent = devices[i];
    select.append(option);
}

