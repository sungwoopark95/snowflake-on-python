# Snowflake on Python

This code enables you to use SQL based on the Snowflake account on python IDE, such as Jupyter Notebook or Pycharm and so on.
These are the steps to use this code:
<ul>
  <li>When you initiate the module, type your snowflake username, password, and account. If you want to specify the warehouse and the database, you may type them in addition.</li>
  <li>There is a public method called 'query_result.' Put a variable, containing a specific query(in a string type) you want to run, into the method as an input</li>
  <li>You can specify the size of the batch. The default size is 'all', thus you can retrieve the result as a whole. Otherwise, you can type the size as much as you want to retrieve.
    <ul>
      <li>For example, if the query is like "select * from table" and the rows you want to retrieve are 10, you can use the method like object_name.query_result("select * from table", size=10)
    </ul>
  </li>
  <li>After you retrieve the result table, you can play with it by using any Pandas methods.</li>
</ul>
