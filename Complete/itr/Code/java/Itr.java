package com.iceberg.randoblock.blocks; 

import net.minecraft.block.Block; 
import net.minecraft.block.SoundType; 
import net.minecraft.block.material.Material; 

public class Itr_ore extends Block { 
 
  public Itr_ore() { 
      super(Properties.create(Material.EARTH).sound(SoundType.GROUND).hardnessAndResistance(3.0f)); 
      setRegistryName("itr_ore"); 
}}