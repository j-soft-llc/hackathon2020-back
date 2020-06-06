from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from initiative.models import Category
from initiative.serializers import FullCategorySerializer, SimpleCategorySerializer


class AllCategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = FullCategorySerializer

    """
                Вернет полный список категорий вместе с дочерними:
                    [
                      {
                        "id": 1,
                        "name": "Коммуналка",
                        "children": [
                          {
                            "id": 4,
                            "name": "Водоснабжение"
                          },
                          {
                            "id": 5,
                            "name": "Тепло"
                          }
                        ]
                      },
                      {
                        "id": 2,
                        "name": "Благоустройство",
                        "children": [
                          {
                            "id": 7,
                            "name": "Дороги"
                          }
                        ]
                      },
                    ]
    """

    def get_queryset(self):
        return self.queryset.select_related('parent')


class HeadingCategoriesListView(ListAPIView):
    """
            Вернет список категорий верхнего уровня (без дочерних):
                [
                  {
                    "id": 1,
                    "name": "Коммуналка"
                  },
                  {
                    "id": 2,
                    "name": "Благоустройство"
                  },
                  {
                    "id": 3,
                    "name": "Соц. сфера"
                  }
                ]
    """
    queryset = Category.objects.filter(parent__isnull=True)
    permission_classes = (IsAuthenticated,)
    serializer_class = SimpleCategorySerializer


class CategoryDetailView(RetrieveAPIView):
    """
        Вернет одну категорию вместе с дочерними, вместо параметра pk нужно подставить id категории:
            {
              "id": 1,
              "name": "Коммуналка",
              "children": [
                {
                  "id": 4,
                  "name": "Водоснабжение"
                },
                {
                  "id": 5,
                  "name": "Тепло"
                }
              ]
            }
    """
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FullCategorySerializer
