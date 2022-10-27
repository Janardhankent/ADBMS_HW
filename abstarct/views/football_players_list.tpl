<html>
<body>
<h2>football_plaayers List</h2>
<hr/>
<table>
% for item in football_players_list:
  <tr>
    <td>{{str(item['desc'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/add" method="post">
  <p>Add new item: <input name="description"/></p>
  <p><button type="submit">Submit</button>
</form>
</body>
</html>