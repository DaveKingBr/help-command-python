@client.command(aliases=['h', 'ajuda'])
async def help(ctx):
  author = ctx.message.author.mention

  embed = discord.Embed(
    title = 'Comandos | DaveBOT',
    description ='Comandos:',
    colour = 6029443
  )

  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/882375933514887181/885329248187977738/images.jpg")

  embed.add_field(name=':exclamation: Prefixo:', value= '**``D!``**', inline=False)

  embed.add_field(name=f':shield:・Moderação:', value='``ban`` **|** ``unban`` **|** ``kick`` **|** ``lock`` **|** ``unlock`` **|** ``addrole`` **|** ``removerole`` **|** ``createrole`` **|** ``serverinfo`` **|** ``deletechannel`` **|** ``createchannel`` ', inline=False)

  embed.add_field(name=':bust_in_silhouette:・Pessoal:', value='``ping``', inline=False)

  embed.add_field(name=':art:・Personalização:', value='``reactrole`` **|** ``avatar``', inline=False)

  embed.add_field(name=':partying_face:・Ações:', value=' ``carinho`` **|** ``tapa`` **|** ``kiss`` **|**   ``dançar`` **|** ``atacar`` ', inline=False)

  embed.add_field(name=f':heart:・Recomendações:', value=f'1- Dê `D!help2` para saber mais sobre meus comandos slash.')

  embed.add_field(name=f':wrench:・Support', value= '**[Suporte Geral](https://discord.gg/PGGrbcWRVH)** **|**  **[Invite](https://discord.com/api/oauth2/authorize?client_id=888117766824030250&permissions=536870911991&scope=bot%20applications.commands)** **|** **[DaveMusic](https://discord.com/api/oauth2/authorize?client_id=888488478545940500&permissions=536870911991&scope=bot)**', inline=False)

  embed.set_footer(text=f'(Reaja algum emoji abaixo para saber mais sobre os comandos do DaveBOT)')

  msg = await ctx.send(author, embed = embed)
  await msg.add_reaction('🛡️')
  await msg.add_reaction('👤')
  await msg.add_reaction('🎨')
  await msg.add_reaction('🥳')
  while True:
    reaction, user = await client.wait_for("reaction_add", timeout=360, check=lambda reaction, user: reaction.message.id == msg.id and user.id == ctx.author.id)
    emoji = str(reaction.emoji)
    if emoji == '🛡️':
      await msg.delete()
      embed = discord.Embed(
        title="Comandos de Moderação",
        description="Sobre os comandos de moderação do DaveBOT.",
        colour=6029443
      )
      embed.add_field(name=':no_entry_sign:・Ban', value='Bani alguém do Servidor. Exemplo: `D!ban @user Motivo`. ', inline=True)
      embed.add_field(name='<a:849237341729194027:890624733568196609>・Unban', value='Desbani alguém do Servidor. Exemplo: `D!unban (Nome e tag do banido)`.', inline=False)
      embed.add_field(name=':x:・Kick', value='Expulsa alguém do servidor. Exemplo: `D!kick @user Motivo`.', inline=False)
      embed.add_field(name=':lock:・Lock', value='Fecha um canal do servidor. Exemplo: `D!lock`.', inline=False)
      embed.add_field(name=':unlock:・Unlock', value='Abre novamente um canal do servidor. Exemplo: `D!unlock`.', inline=False)
      embed.add_field(name=':tada:・AddRole', value='Adiciona um cargo ao usuário. Exemplo: `D!addrole @user`.', inline=False)
      embed.add_field(name=':arrow_down:・RemoveRole', value='Remove um cargo do usuário. Exemplo: `D!removerole @user`', inline=False)
      embed.add_field(name=':briefcase:・CreateRole', value='Cria um cargo no servidor. Exemplo: `D!createrole (Nome do cargo)`.', inline=False)
      embed.add_field(name=':exclamation:・ServerInfo', value='Mostra as informações públicas do servidor. Exemplo: `D!serverinfo`', inline=False)
      embed.add_field(name=':arrow_down:・DeleteChannel', value='Deleta um canal do servidor. Exemplo: `D!deletechannel #canal`', inline=False)
      embed.add_field(name=':thumbsup:・CreateChannel', value='Cria um canal no servidor. Exemplo: `D!createchannel (Nome do canal)`.', inline=True)

      embed.set_footer(text=f'Author: {ctx.author}')
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/888095776335597599/890649616381534268/images.jpg')

      mensagem = await ctx.send(author, embed=embed)
    if emoji == '👤':
      await msg.delete()
      embed = discord.Embed(
        title='Comandos Pessoais',
        description='Sobre os Comandos Pessoais',
        colour=6029443
      )
      embed.add_field(name=':exclamation:・Ping', value='Veja a sua quantidade de ms nesse exato momento por esse comando. Exemplo: `D!ping`.')
      embed.set_footer(text=f'Author: {ctx.author} ')
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/888095776335597599/890649616381534268/images.jpg')

      await ctx.send(author, embed = embed)
