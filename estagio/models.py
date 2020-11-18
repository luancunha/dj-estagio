from django.db import models

class faculdades(models.Model):
    codigo = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'faculdades'
        verbose_name = 'Cad.Faculdade'

class cursos(models.Model):
    codigo = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=50)
    departamento = models.CharField(max_length=30)
    faculdade = models.ForeignKey('faculdades', db_column='faculdade', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'cursos'
        verbose_name = 'Cad.Curso'

class profcoorest(models.Model):
    masp = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey('cursos', db_column='curso', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'profcoorest'
        verbose_name = 'Cad.Profcoorest'

class alunos(models.Model):
    matricula = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    datanasc = models.DateField()
    periodo = models.IntegerField()
    curso = models.ForeignKey('cursos', db_column='curso', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'alunos'
        verbose_name = 'Cad.Aluno'

class estagio(models.Model):
    codigo = models.AutoField(primary_key = True)
    aluno = models.ForeignKey('alunos', db_column='aluno', on_delete=models.CASCADE)
    profest = models.ForeignKey('profcoorest', db_column='profest', on_delete=models.CASCADE)
    remunerado = models.CharField(max_length=1)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    empresa = models.CharField(max_length=30)
    cargahr = models.IntegerField()
    descr_est = models.CharField(max_length=256)
    resp_est = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s' % (self.codigo)
        
    class Meta:
        managed = False
        db_table = 'estagio'
        verbose_name = 'Cad.Estagio'