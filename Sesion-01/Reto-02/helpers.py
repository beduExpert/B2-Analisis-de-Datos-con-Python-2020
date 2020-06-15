
def verificar_resultados(df_meteoritos, promedio_diametro, mediana_diametro):
    promedio = df_meteoritos['estimated_diameter.meters.estimated_diameter_max'].mean()
    if promedio_diametro != promedio:
        print(f'El promedio no fue calculado correctamente.')
        print(f'Promedio esperado: {promedio}; Promedio recibido: {promedio_diametro}')
        return
        

    mediana = df_meteoritos['estimated_diameter.meters.estimated_diameter_max'].median()
    if mediana_diametro != mediana:
        print(f'La mediana no fue calculada correctamente.')
        print(f'Mediana esperada: {mediana}; Mediana recibida: {mediana_diametro}')
        return
        
    print(f'Los estimados fueron calcualados correctamente.\n')
    print(f'El promedio calculado fue de {promedio_diametro} mientras que la mediana fue de {mediana_diametro}.')
    print(f'¿A qué le atribuyes tú la diferencia?')