window.onload = function() {
    var devices = JSON.parse(document.getElementById('name_var').textContent);
    var groupes = JSON.parse(document.getElementById('groupe_var').textContent);
    var subjectSel = document.getElementById("groupe");
    var topicSel = document.getElementById("name");
    var i
    for (i = 0; i < groupes.length; i++) {
        subjectSel.options[subjectSel.options.length] = new Option(groupes[i], groupes[i]);
    }
    subjectSel.onchange = function() {
        topicSel.length = 0;
        //display correct values
        var i
        for (i = 0; i < devices.length; i++) {
        split = devices[i].split(',');
        if (split[1].search(this.value) != -1){
            topicSel.options[topicSel.options.length] = new Option(split[0], split[0]);
        }
        if (this.value === '/'){
            topicSel.options[topicSel.options.length] = new Option(split[0], split[0]);
        } 
      }
    }
}




// var groupes = JSON.parse(document.getElementById('groupe_var').textContent);
// select_groupe = document.getElementById('groupe')

// var i;
// for (i = 0; i < groupes.length; i++) {
//     option = document.createElement('option');
//     option.setAttribute("value", groupes[i]);
//     option.textContent = groupes[i];
//     select_groupe.append(option);
// }

var tags = JSON.parse(document.getElementById('tag_var').textContent);
select_tag = document.getElementById('tag')

var i;
for (i = 0; i < tags.length; i++) {
    option = document.createElement('option');
    option.setAttribute("value", tags[i]);
    option.textContent = tags[i];
    select_tag.append(option);
}


var types = JSON.parse(document.getElementById('names').textContent);
var datas = JSON.parse(document.getElementById('data').textContent);
let body = document.body;

type_message = document.getElementById('type_message').textContent;

if (type_message[1] == 0){
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
        k = 0;
        for (j = 0; j < names.length; j++) {
            tmp = document.createElement('th');
            tmp.textContent = names[j];
            thead.append(tmp);    
            tmp = document.createElement('td');
            if (types[i][2][j] == 0){ 
                tmp.textContent = data[k];}
            else{
                if (types[i][2][j] == 3){
                    tmp.textContent = '202'+data[k]+'/'+data[k+1]+'/'+data[k+2]
                    k += 2
                }else{
                    tmp.textContent = data[k]+':'+data[k+1]
                    k += 1
                }
            }
            tbody.append(tmp); 
            table.append(thead,tbody);
            k++;
        }
        body.append(table);
    }
}else{
    table = document.createElement('table');
    table.setAttribute("class", 'table');
    thead = document.createElement('thead');
    tbody = document.createElement('tbody');
    tr = document.createElement('tr');
    th = document.createElement('th');
    th.setAttribute('colspan','100%');
    th.textContent = types[0][0];
    tr.append(th);
    thead.append(tr); 
    names = types[0][1].split(',');
    var i;
    for (j = 0; j < names.length; j++) {
        tmp = document.createElement('th');
        tmp.textContent = names[j];
        thead.append(tmp);    
        }
    for (i = 0; i < types.length; i++) {
        tr = document.createElement('tr');
        data = datas[i];
        k = 0;
        for (j = 0; j < names.length; j++) {    
            tmp = document.createElement('td');
            if (types[i][2][j] == 0){ 
                tmp.textContent = data[k];}
            else{
                if (types[i][2][j] == 3){
                    tmp.textContent = '202'+data[k]+'/'+data[k+1]+'/'+data[k+2]
                    k += 2
                }else{
                    tmp.textContent = data[k]+':'+data[k+1]
                    k += 1
                }
            }
            tr.append(tmp); 
            k++;
        }
        tbody.append(tr);
    }
    table.append(thead,tbody);
    body.append(table);
}