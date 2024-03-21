<script>
    import ToggleButton from "./ToggleButton.svelte";

</script>

<header class="site-header">
    <nav class="main-nav">
        <ul class="nav-list-left">
            
            <li class="nav-item"><a href="/">Главная</a></li>
            <li class="nav-item"><a href="/about">О нас</a></li>
            <li class="nav-item"><a href="/contactus">Контакты</a></li>
        </ul>
        <ul class="nav-list-right">
            <li class="nav-item"><a href="/reg">Регистрация</a></li>
            <li class="nav-item"><a href="/login">Войти</a></li>
            <li class="nav-item"><ToggleButton /></li>
            
        </ul>
    </nav>
</header>

<style>

.site-header {
    background-color: transparent;
    padding: 10px ;
}

.main-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.main-nav .nav-list-left {
    list-style: circle;
}

.main-nav .nav-list-right {
    list-style: circle;
    text-align: right;
}

.nav-item {
    display: inline;
    margin: 0 10px;
}



</style>