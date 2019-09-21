package com.iceberg.randoblock.blocks; 

import com.iceberg.randoblock.Main; 
net.minecraft.item.Item; 
public class Itr extends Item { 
   public Itr() { 
       super(new Item.Properties().maxStackSize(64).group(Main.setup.itemGroup) 
       setRegistryName("itr"); 
}}