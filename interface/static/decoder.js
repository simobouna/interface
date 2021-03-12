var types = JSON.parse(document.getElementById('names').textContent);
var datas = JSON.parse(document.getElementById('data').textContent);
let body = document.body;


var i;
for (i = 0; i < types.length; i++) {
    table = document.createElement('table');
    table.setAttribute("class", 'table');
    thead = document.createElement('thead');
    tr = document.createElement('tr');
    th = document.createElement('th');
    th.setAttribute('colspan','100%');
    th.textContent = types[i][0];
    tr.append(th);
    thead.append(tr); 
    tbody = document.createElement('tbody');
    names = types[i][1].split(',');
    data = datas[i];
    for (j = 0; j < names.length; j++) {
        tmp = document.createElement('th');
        tmp.textContent = names[j];
        thead.append(tmp);    
        tmp = document.createElement('td');
        tmp.textContent = data[j];
        tbody.append(tmp); 
        table.append(thead,tbody);
    }
    body.append(table);
}
