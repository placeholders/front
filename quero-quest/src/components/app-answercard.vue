<template>
  <vk-card>
    <div class="body">
      <div class="title">
        <h3>placeholder problem title</h3>
      </div>
      <div class="vote">
      <img src="@/assets/upvote.png" @click="upvote"/>
      <div class="votes" id="voted">
      <img src="@/assets/questing.png"/>
      </div>
      <div class="vote" id="votet">
      <img src="@/assets/downvote.png" @click="downvote"/>
      <span class="label label-primary">{{ votes }}</span>
      </div>
    </div>
      <div class="desc small-text">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit eos neque non facilis tempora reprehenderit harum animi sint necessitatibus minima? Cum tenetur veniam harum porro maiores exercitationem accusantium, praesentium magnam commodi, cupiditate ducimus asperiores adipisci. Aliquid, repellat repudiandae voluptatem eos dolore cumque quas nostrum, perferendis doloremque, aliquam accusantium placeat eaque?</p>
      </div>
      <div class="desc small small-text">
        <p> Answer Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit eos neque non facilis tempora reprehenderit harum animi sint necessitatibus minima? Cum tenetur veniam harum porro maiores exercitationem accusantium, praesentium magnam commodi, cupiditate ducimus asperiores adipisci. Aliquid, repellat repudiandae voluptatem eos dolore cumque quas nostrum, perferendis doloremque, aliquam accusantium placeat eaque?</p>
      </div>
      <div class="desc small small-text">
        Nome henrique estefano de messias
    </div>
  </vk-card>
</template>
