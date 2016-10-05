<!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en-US"> <![endif]-->
<!--[if IE 7]> <html class="no-js lt-ie9 lt-ie8" lang="en-US"> <![endif]-->
<!--[if IE 8]> <html class="no-js ie8 lt-ie9" lang="en-US"> <![endif]-->
<!--[if IE 9]> <html class="no-js ie9" lang="en-US"><![endif]-->
<!--[if gt IE 9]><!-->
<html lang="nl-NL"><!--<![endif]-->

<!--
whale 1.0
BY LABEL A
-->
    <%include file="whale:templates/inc/html_head.mako" />

<body>

    ${self.body()}


<script src="${request.static_url('whale:static/js/libs/jquery.min.js')}"></script>
<script src="${request.static_url('whale:static/js/libs/bootstrap.min.js')}"></script>
<script>
    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
                    (i[r].q = i[r].q || []).push(arguments)
                }, i[r].l = 1 * new Date();
        a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    // Replace with your own google analytics code
    ga('create', 'XX-XXXXXXX-X', 'auto');
    ga('send', 'pageview');
</script>

    <%block name="scripts"></%block>

</body>
</html>
