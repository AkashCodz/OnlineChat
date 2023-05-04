from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Chat, Group
from channels.db import database_sync_to_async          # database work 'imp'

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('WebSocket Connected...')
        print('channel layer...',self.channel_layer)
        print('channel name...',self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['root_name']  # 'root_name' can be changed 
        print('Group name...',self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        self.user_profile = self.scope['user']
        # user_profile = await database_sync_to_async(UserProfile.objects.get)(pk=self.scope['user'].pk)
        # message = {
        #     'name': self.user_profile,
        #     'gender': self.user_profile.gen,
        #     'country': self.user_profile.con
        # }
        # print(message)
        # self.send(text_data=json.dumps(message))
        
    async def receive_json(self, content, **kwargs):
        print('Message Received from Client...', content)
        ################Database work #####################
        group = await database_sync_to_async( Group.objects.get)(name=self.group_name)
        #----------------Authentication-------------------#
        if self.scope['user'].is_authenticated:
            chat = Chat(
                content = content['msg'],
                group = group
            )
            await database_sync_to_async( chat.save)()
            ###################################################
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': content['msg']
                }
            )
        else:
            await self.send_json({'msg':'Login Required'})
        #-----------------------------------------------#
        
    async def chat_message(self,event):
        print('Event...',event)
        await self.send_json({'message':event['message']}) 
    
    async def disconnect(self, close_code):
        print('Websocket Disconnect...', close_code)
        print('channel layer...',self.channel_layer)
        print('channel name...',self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    # @database_sync_to_async
    # def update_user_incr(self, user):
    #     Group.objects.filter(pk=user.pk).update(online=('online') + 1)

    # @database_sync_to_async
    # def update_user_decr(self, user):
    #     Group.objects.filter(pk=user.pk).update(online=('online') - 1)