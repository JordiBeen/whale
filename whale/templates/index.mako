<%inherit file="whale:templates/inc/main.mako"/>

<div class="container">
    <h1>Hello World.</h1>

    <p>You did it!</p>
    <p>You have started a new Pyramid project with the name: whale.</p>
    <p>There's actually a user your the database as well: ${user.firstname} ${user.infix} ${user.lastname}</p>
</div>

<%block name="scripts">
    <script src="${request.static_url('whale:static/js/script.js')}"></script>
</%block>
