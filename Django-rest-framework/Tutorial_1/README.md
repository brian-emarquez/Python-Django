## Django REST framework


* Install

```python
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

<table align="center">
  <tr>
    <td align="center" style="padding=0;width=50%;">
      <img align="center" style="padding=0;" src="./imagesReadme/rest.png" />
    </td>
  </tr>
</table>

Serializers

Documentation [Serializers](https://www.django-rest-framework.org/tutorial/quickstart/#serializers)

Notice that we're using hyperlinked relations in this case with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.