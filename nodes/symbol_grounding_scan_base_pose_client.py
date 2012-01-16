#!/usr/bin/env python
import roslib; roslib.load_manifest('srs_symbolic_grounding')

from srs_symbolic_grounding.srv import *
from srs_symbolic_grounding.msg import *
from geometry_msgs.msg import *
import rospy



def symbol_grounding_scan_base_pose_client(parent_obj_geometry, furniture_geometry_list):

	rospy.wait_for_service('symbol_grounding_scan_base_pose')
	
	symbol_grounding_scan_base_pose = rospy.ServiceProxy('symbol_grounding_scan_base_pose', SymbolGroundingScanBasePose)
	
	try:
		resp = list()
		resp.append(symbol_grounding_scan_base_pose(parent_obj_geometry, furniture_geometry_list))
		return resp
	
	except rospy.ServiceException, e:
		
		print "Service call failed: %s" %e



def getWorkspaceOnMap():
	print 'test get all workspace (furnitures basically here) from map'
	try:
		requestNewTask = rospy.ServiceProxy('get_workspace_on_map', GetWorkspaceOnMap)
		res = requestNewTask('ipa-kitchen-map', True)
		return res
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

if __name__ == "__main__":

	workspace_info = getWorkspaceOnMap()	
	
	parent_obj_geometry = SRSSpatialInfo()
	
	parent_obj_geometry.pose.position.x = workspace_info.objectsInfo[5].pose.position.x
	parent_obj_geometry.pose.position.y = workspace_info.objectsInfo[5].pose.position.y
	parent_obj_geometry.pose.position.z = workspace_info.objectsInfo[5].pose.position.z
	parent_obj_geometry.pose.orientation.x = workspace_info.objectsInfo[5].pose.orientation.x
	parent_obj_geometry.pose.orientation.y = workspace_info.objectsInfo[5].pose.orientation.y
	parent_obj_geometry.pose.orientation.z = workspace_info.objectsInfo[5].pose.orientation.z
	parent_obj_geometry.pose.orientation.w = workspace_info.objectsInfo[5].pose.orientation.w
	parent_obj_geometry.l = workspace_info.objectsInfo[5].l
	parent_obj_geometry.w = workspace_info.objectsInfo[5].w
	parent_obj_geometry.h = workspace_info.objectsInfo[5].h

	furniture_geometry_list = list()
	furniture_geometry_list = workspace_info.objectsInfo


	print "Requesting scan base pose."
	
	result = symbol_grounding_scan_base_pose_client(parent_obj_geometry, furniture_geometry_list)
	
	print result
		


