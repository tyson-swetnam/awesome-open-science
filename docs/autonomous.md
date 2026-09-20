---
description: Simulators, digital twins, and autonomy stacks for ground, aerial, and marine robotics.
---

# :material-robot-industrial: Autonomous Systems & Robotics

Open source simulators, digital twins, and autonomy stacks for ground, aerial, and marine
robotics. These tools let researchers train and evaluate perception and control policies
reproducibly, without privileged hardware access.

!!! Note "See also"

    [Hardware](hardware.md) lists autopilot firmware and uncrewed systems
    hardware. This page covers the simulation, digital twin, and autonomy software that runs
    against it.

## :material-car-connected: Ground Vehicle Simulators & Digital Twins

[CARLA](https://carla.org/){target=_blank} - autonomous driving simulator built on Unreal Engine, with configurable sensor suites, traffic scenarios, and ROS bridges for perception and reinforcement learning research. MIT licensed and the most widely adopted open simulator in the field

[AWSIM](https://github.com/tier4/AWSIM){target=_blank} - Unity-based digital twin simulator from TIER IV, built for end-to-end validation of Autoware stacks over ROS 2

[AlpaSim](https://github.com/NVlabs/alpasim){target=_blank} - NVIDIA closed-loop simulation platform for developing and testing end-to-end autonomous vehicle policies, using neural rendering for sensor simulation and gRPC microservices for each subsystem. Apache 2.0

[AutoDRIVE](https://autodrive-ecosystem.github.io/){target=_blank} - lightweight digital twin ecosystem pairing scaled physical vehicles with a matching simulator, aimed at autonomy research that cannot justify full-scale hardware

## :material-cube-scan: Digital Twin Generation & Physics

[OpenTwinMap](https://github.com/jmscslgroup/OpenTwinMap){target=_blank} - generates 3D semantic road meshes for simulators from OpenStreetMap and LiDAR input, with a CARLA plugin for loading the output. Early stage; see the [paper](https://arxiv.org/abs/2511.21925){target=_blank}

[NVIDIA PhysX](https://github.com/NVIDIA-Omniverse/PhysX){target=_blank} - real-time physics engine for rigid body dynamics and collision, underpinning vehicle dynamics in several robotics simulators. BSD-3

## :material-highway: Autonomy Stacks & Driving Foundation Models

[Autoware](https://autoware.org/){target=_blank} - full-stack open source autonomous driving software built on ROS 2, governed by the Autoware Foundation

- [autoware_universe](https://github.com/autowarefoundation/autoware_universe){target=_blank} - the actively developed component repository. Autoware.Auto, the earlier architecture, is retired

[NVIDIA Alpamayo](https://github.com/NVlabs/alpamayo){target=_blank} - open 10B vision-language-action model that pairs driving trajectories with chain-of-causation reasoning traces, for research on edge-case decision making. Inference code is Apache 2.0; weights are released under OpenMDW-1.1. Renamed from Alpamayo-R1 at CES 2026

## :material-quadcopter: Aerial (UAV) Simulation

[PX4 Simulation](https://docs.px4.io/main/en/simulation/){target=_blank} - software-in-the-loop simulation for the PX4 autopilot, with backends including Gazebo and jMAVSim for testing vision and path planning

[ArduPilot SITL](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html){target=_blank} - software-in-the-loop simulator modeling flight physics, environmental conditions, and sensor noise without any flight hardware

[Flightmare](https://github.com/uzh-rpg/flightmare){target=_blank} - quadrotor simulator from UZH that decouples rendering from physics, enabling the throughput needed for reinforcement learning. Last released 2024

## :material-submarine: Marine (AUV/ROV) Simulation

[Stonefish](https://github.com/patrykcieslak/stonefish){target=_blank} - C++ simulation library for marine robotics with hydrodynamics and acoustic sensor models, and the most actively maintained option here. GPL-3

[Plankton](https://github.com/Liquid-ai/Plankton){target=_blank} - ROS 2 port of the UUV Simulator, carrying the underwater vehicle models forward to current middleware. Apache 2.0; last released 2024

[UUV Simulator](https://uuvsimulator.github.io/){target=_blank} - Gazebo and ROS package for underwater digital twins with buoyancy, hydrodynamics, and sonar modeling. Archived in 2023 and superseded by Plankton; listed for provenance
