## Django REST framework

<table align="center">
  <tr>
    <td align="center" style="padding=0;width=50%;">
      <img align="center" style="padding=0;" src="././images/rest.png" />
    </td>
  </tr>
</table>

* Comands

*Use Freeze*

```diff
pip freeze > requirements.txt
```

*Use django*

```diff
pip install django
```

*Use djangorestframework*

```diff
pip install djangorestframework
```

*Use pygments*

```diff
pip install pygments
```



---

* Serializers

Documentation [Serializers](https://www.django-rest-framework.org/tutorial/quickstart/#serializers)

Notice that we're using hyperlinked relations in this case with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.