from django.db import models

# Create your models here.

#标签
class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField('标签名',max_length=32,unique=True)
    label_color = models.CharField('标签颜色',max_length=32,blank=True)
    label_hover_color = models.CharField('标签hover颜色',max_length=32,blank=True)
    label_time = models.DateTimeField('创建时间',auto_now_add=True)

    def __str__(self):
        return self.label_name

    class Meta:
        db_table = 'Label'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


#实体
class Entity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_name = models.CharField('实体名称',max_length=32,unique=True)
    entity_label = models.ForeignKey(Label,
                                      on_delete=models.CASCADE,
                                      verbose_name='标签'
                                       )
    entity_notes = models.CharField('注释',max_length=108,blank=True)
    entity_color = models.CharField('实体颜色',max_length=32,blank=True)
    entity_time = models.DateTimeField('创建时间',auto_now_add=True)

    def __str__(self):
        return self.entity_name

    class Meta:
        db_table = 'Entity'
        verbose_name = '实体'
        verbose_name_plural = verbose_name


#关系
class RelationShip(models.Model):
    relationship_id = models.AutoField(primary_key=True)
    relationship_name = models.CharField('关系',max_length=32,unique=True)
    relationship_entities = models.ManyToManyField('self',symmetrical=False,through='Label_RelationShip')

    def __str__(self):
        return self.relationship_name

    class Meta:
        db_table = 'RelationShip'
        verbose_name = '关系'
        verbose_name_plural = verbose_name


#标签-关系
class Label_RelationShip(models.Model):
    lr_id = models.AutoField(primary_key=True)
    lr_labelA = models.ForeignKey(Label,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  related_name='lr_labelA_set',
                                  verbose_name='标签A'
                                  )
    lr_labelB = models.ForeignKey(Label,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  related_name='lr_labelB_set',
                                  verbose_name='标签B'
                                  )
    lr_relationship = models.ForeignKey(RelationShip,
                                        on_delete=models.CASCADE,
                                        verbose_name='关系'
                                        )
    lr_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'LR'
        verbose_name = '标签-关系'
        verbose_name_plural = verbose_name


