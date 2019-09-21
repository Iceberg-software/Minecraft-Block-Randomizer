package com.iceberg.randoblock.blocks; 

import net.minecraft.block.Block; 
import net.minecraft.block.SoundType; 
import net.minecraft.block.material.Material; 

public class Iovsp_ore extends Block { 

  public Iovsp_ore() { 
      super(Properties.create(Material.EARTH).sound(SoundType.GROUND).hardnessAndResistance(3.0f)); 
      setRegistryName("iovsp_ore"); 
}}