def printX(a):
  print(a)
  
def grafikon(fx,desc1,txt1,desc2="",txt2="",ngraf=2,c1='rgba(0,200,0,0.8)', c2='rgba(200,0,0,0.3)'):
    '''
    grafikon(fx,desc1,txt1,desc2="",txt2="",ngraf=2,c1='rgba(0,200,0,0.8)', c2='rgba(200,0,0,0.3)')

    fx: dataFrame
    desc1:column1
    txt1: label1
    desc2:column2
    txt2: label2
    ngraf: number of graph
    c2: color1
    c2: color2

    '''
    #x_=[i for i in range(len(y_pred))]

    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    fig0 = make_subplots(rows=1, cols=1,)
    
    fig0.add_trace(
        go.Scatter(x=fx.index, y=fx[desc1], name=txt1,line=dict(color=c1) ,showlegend=True  ),

        row=1, col=1

    )
    
    if ngraf==2:
        fig0.add_trace(
            go.Scatter(x=fx.index, y=fx[desc2], name=txt2, line=dict(color=c2) ,showlegend=True  ),

            row=1, col=1
        )
    
    fig0.update_layout(
        autosize=False,
        width=1200,
        height=600,
        )

    fig0.show()
