import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InvcGrpSvc
# Description: AR Invoice Group
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_InvcGrps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvcGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps",headers=creds) as resp:
           return await resp.json()

async def post_InvcGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InvcGrps_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcGrp item
   Description: Calls GetByID to retrieve the InvcGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InvcGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InvcGrp for the service
   Description: Calls UpdateExt to update InvcGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InvcGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InvcGrp item
   Description: Call UpdateExt to delete InvcGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvcGrps_Company_GroupID_InvcGrpAttches(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InvcGrpAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InvcGrpAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")/InvcGrpAttches",headers=creds) as resp:
           return await resp.json()

async def get_InvcGrps_Company_GroupID_InvcGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcGrpAttch item
   Description: Calls GetByID to retrieve the InvcGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcGrpAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvcGrpAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvcGrpAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcGrpAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches",headers=creds) as resp:
           return await resp.json()

async def post_InvcGrpAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcGrpAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InvcGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcGrpAttch item
   Description: Calls GetByID to retrieve the InvcGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InvcGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InvcGrpAttch for the service
   Description: Calls UpdateExt to update InvcGrpAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InvcGrpAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InvcGrpAttch item
   Description: Call UpdateExt to delete InvcGrpAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcGrpAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseInvcGrp, whereClauseInvcGrpAttch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInvcGrp=" + whereClauseInvcGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInvcGrpAttch=" + whereClauseInvcGrpAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsUseLockSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsUseLockSetting
   Description: Returns the InvcGrp dataset using the automatic group lock configuration setting.
   OperationID: GetRowsUseLockSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsUseLockSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUseLockSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsBOEGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsBOEGrp
   Description: Validate if the group is used for Bill of Exchange.
   OperationID: IsBOEGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsBOEGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsBOEGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsLocked
   Description: Validate if the group is locked.
   OperationID: IsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvcGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvcGrp
   Description: Sets the user lock on the Current group. This method also run GetByID..
   OperationID: GetInvcGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvcGrpForBOE(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvcGrpForBOE
   Description: Sets the user lock on the Current group. This method also run GetByID.
Used for Bill of Exchange Entry
   OperationID: GetInvcGrpForBOE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvcGrpForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcGrpForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForBOE(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForBOE
   Description: Sets the user lock on the Current group. This method also run GetByID..
   OperationID: GetListForBOE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForGUI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForGUI
   Description: Get the list of groups for Taiwan GUI.
   OperationID: GetListForGUI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForGUI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForGUI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRMACRREQGroup(epicorHeaders = None):
   """  
   Summary: Invoke method GetRMACRREQGroup
   Description: This method should ONLY be called for RMA processing.  It creates a group
with a groupid of RMACRREQ.  This group cannot be updated.
   OperationID: GetRMACRREQGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMACRREQGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofApplyDate
   Description: This methods should be called to validate the new apply date entered by
the user.
   OperationID: OnChangeofApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofInvoiceDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofInvoiceDate
   Description: This methods should be called to validate the new invoice date entered by
the user.
   OperationID: OnChangeofInvoiceDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofInvoiceDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofInvoiceDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostInvoices
   Description: Posts the invoices for a group.
   OperationID: PostInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePostInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePostInvoices
   Description: This method should be called before Invoices for a group are posted. If the GL
is not interfaced the user will be asked to continue Y/N.  If they choose N,
the PostInvoices method should not be called.
   OperationID: PrePostInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockGroup
   Description: Clears the lock of a group, only if the user of the current session is the same as the one locking the group.
This method update the database and refresh the group dataset with the information from the database.
   OperationID: UnlockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockGroup
   Description: Locks the groupID for the current user in session only if the group is not locked already
This method update the database and refresh the group dataset with the information from the database.
   OperationID: LockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateForBOE(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateForBOE
   Description: Sets the user lock on the Current group. This method also run GetByID.
Used for Bill of Exchange Entry
   OperationID: UpdateForBOE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckNewGroupIDForBOE(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckNewGroupIDForBOE
   Description: Verifies that group with specified group id could be an AR Bill Of Exchange Group.
   OperationID: CheckNewGroupIDForBOE
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckNewGroupIDForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNewGroupIDForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateNoLock
   Description: Update group without locking by ActiveUser
   OperationID: UpdateNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsNoLock
   Description: The wrapper method for GetRows. Retrieve groups ignoring Active User lock
   OperationID: GetRowsNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcGrpAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcGrpAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcGrpAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcGrpAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcGrpAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcGrpAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcGrpRow] = obj["value"]
      pass

class Erp_Tablesets_InvcGrpAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.UpdateInvAutoPrint:bool = obj["UpdateInvAutoPrint"]
      """  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.AutoPrintEDIOnly:bool = obj["AutoPrintEDIOnly"]
      """  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BOEPost:str = obj["BOEPost"]
      """  BOE Post  """  
      self.IsBOE:bool = obj["IsBOE"]
      """  Is BOE  """  
      self.UserCanPostGroupFlag:bool = obj["UserCanPostGroupFlag"]
      """  Flag to allow the user to post based on security.  """  
      self.UserCanDeposit:bool = obj["UserCanDeposit"]
      """  Flag to indicate whether the use can create a deposit.  """  
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      """  Total amount for invoices in this group.  """  
      self.FromBOE:bool = obj["FromBOE"]
      """  Indicates whether this dataset's row comes from Bill Of Exchange or not.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.UpdateInvAutoPrint:bool = obj["UpdateInvAutoPrint"]
      """  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.AutoPrintEDIOnly:bool = obj["AutoPrintEDIOnly"]
      """  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BOEPost:str = obj["BOEPost"]
      """  BOE Post  """  
      self.IsBOE:bool = obj["IsBOE"]
      """  Is BOE  """  
      self.CashGroupID:str = obj["CashGroupID"]
      """  Cash Group ID  """  
      self.PECollectionMode:int = obj["PECollectionMode"]
      """  PECollectionMode  """  
      self.PECollectionCustNum:int = obj["PECollectionCustNum"]
      """  PECollectionCustNum  """  
      self.FromBOE:bool = obj["FromBOE"]
      """  Indicates whether this dataset's row comes from Bill Of Exchange or not.  """  
      self.IsDocumentLocked:bool = obj["IsDocumentLocked"]
      """  is invcGrp locked in RvLock table.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted. an invoice is already in review journal or in posting process.  """  
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      """  Total amount for invoices in this group.  """  
      self.UserCanDeposit:bool = obj["UserCanDeposit"]
      """  Flag to indicate whether the use can create a deposit.  """  
      self.UserCanPostGroupFlag:bool = obj["UserCanPostGroupFlag"]
      """  Flag to allow the user to post based on security.  """  
      self.ChkCollections:bool = obj["ChkCollections"]
      """   Indicates if the check of invoices customers being in Collections needs to be done before the Post
(Used for Peru localization)  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckNewGroupIDForBOE_input:
   """ Required : 
   GroupID
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      pass

class CheckNewGroupIDForBOE_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.Message:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_InvcGrpAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.UpdateInvAutoPrint:bool = obj["UpdateInvAutoPrint"]
      """  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.AutoPrintEDIOnly:bool = obj["AutoPrintEDIOnly"]
      """  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BOEPost:str = obj["BOEPost"]
      """  BOE Post  """  
      self.IsBOE:bool = obj["IsBOE"]
      """  Is BOE  """  
      self.UserCanPostGroupFlag:bool = obj["UserCanPostGroupFlag"]
      """  Flag to allow the user to post based on security.  """  
      self.UserCanDeposit:bool = obj["UserCanDeposit"]
      """  Flag to indicate whether the use can create a deposit.  """  
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      """  Total amount for invoices in this group.  """  
      self.FromBOE:bool = obj["FromBOE"]
      """  Indicates whether this dataset's row comes from Bill Of Exchange or not.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcGrpListTableset:
   def __init__(self, obj):
      self.InvcGrpList:list[Erp_Tablesets_InvcGrpListRow] = obj["InvcGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvcGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  """  
      self.PostInProcess:bool = obj["PostInProcess"]
      """  Field to lock the InvcGrp record while the Post Process is running.  """  
      self.UpdateInvAutoPrint:bool = obj["UpdateInvAutoPrint"]
      """  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.AutoPrintEDIOnly:bool = obj["AutoPrintEDIOnly"]
      """  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BOEPost:str = obj["BOEPost"]
      """  BOE Post  """  
      self.IsBOE:bool = obj["IsBOE"]
      """  Is BOE  """  
      self.CashGroupID:str = obj["CashGroupID"]
      """  Cash Group ID  """  
      self.PECollectionMode:int = obj["PECollectionMode"]
      """  PECollectionMode  """  
      self.PECollectionCustNum:int = obj["PECollectionCustNum"]
      """  PECollectionCustNum  """  
      self.FromBOE:bool = obj["FromBOE"]
      """  Indicates whether this dataset's row comes from Bill Of Exchange or not.  """  
      self.IsDocumentLocked:bool = obj["IsDocumentLocked"]
      """  is invcGrp locked in RvLock table.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted. an invoice is already in review journal or in posting process.  """  
      self.TotalInvAmt:int = obj["TotalInvAmt"]
      """  Total amount for invoices in this group.  """  
      self.UserCanDeposit:bool = obj["UserCanDeposit"]
      """  Flag to indicate whether the use can create a deposit.  """  
      self.UserCanPostGroupFlag:bool = obj["UserCanPostGroupFlag"]
      """  Flag to allow the user to post based on security.  """  
      self.ChkCollections:bool = obj["ChkCollections"]
      """   Indicates if the check of invoices customers being in Collections needs to be done before the Post
(Used for Peru localization)  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcGrpTableset:
   def __init__(self, obj):
      self.InvcGrp:list[Erp_Tablesets_InvcGrpRow] = obj["InvcGrp"]
      self.InvcGrpAttch:list[Erp_Tablesets_InvcGrpAttchRow] = obj["InvcGrpAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtInvcGrpTableset:
   def __init__(self, obj):
      self.InvcGrp:list[Erp_Tablesets_InvcGrpRow] = obj["InvcGrp"]
      self.InvcGrpAttch:list[Erp_Tablesets_InvcGrpAttchRow] = obj["InvcGrpAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

class GetInvcGrpForBOE_input:
   """ Required : 
   inGroupID
   ds
   """  
   def __init__(self, obj):
      self.inGroupID:str = obj["inGroupID"]
      """  Group ID.  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class GetInvcGrpForBOE_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetInvcGrp_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class GetInvcGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetListForBOE_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetListForBOE_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForGUI_input:
   """ Required : 
   whereClause
   tranDocTypeID
   startDate
   endDate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      """  tranDocTypeID  """  
      self.startDate:str = obj["startDate"]
      """  startDate  """  
      self.endDate:str = obj["endDate"]
      """  endDate  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetListForGUI_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInvcGrpAttch_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewInvcGrpAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInvcGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class GetNewInvcGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRMACRREQGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

class GetRowsNoLock_input:
   """ Required : 
   whereClauseInvcGrp
   whereClauseInvcGrpAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInvcGrp:str = obj["whereClauseInvcGrp"]
      self.whereClauseInvcGrpAttch:str = obj["whereClauseInvcGrpAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsUseLockSetting_input:
   """ Required : 
   whereClauseInvcGrp
   whereClauseInvcGrpAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInvcGrp:str = obj["whereClauseInvcGrp"]
      """  InvcGrp where clause  """  
      self.whereClauseInvcGrpAttch:str = obj["whereClauseInvcGrpAttch"]
      """  Attachment where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsUseLockSetting_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseInvcGrp
   whereClauseInvcGrpAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInvcGrp:str = obj["whereClauseInvcGrp"]
      self.whereClauseInvcGrpAttch:str = obj["whereClauseInvcGrpAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class IsBOEGrp_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      pass

class IsBOEGrp_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsLocked_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID to check if is locked.  """  
      pass

class IsLocked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if group is locked, otherwise false.  """  
      pass

class LockGroup_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID to lock  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class LockGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofApplyDate_input:
   """ Required : 
   groupID
   newApplyDate
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      self.newApplyDate:str = obj["newApplyDate"]
      """  New Apply Date.  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class OnChangeofApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofInvoiceDate_input:
   """ Required : 
   groupID
   newInvoiceDate
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      self.newInvoiceDate:str = obj["newInvoiceDate"]
      """  New invoice date.  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class OnChangeofInvoiceDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostInvoices_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      pass

class PostInvoices_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.invoicesGenerated:str = obj["parameters"]
      self.errorMessage:str = obj["parameters"]
      self.legalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PrePostInvoices_input:
   """ Required : 
   ipTCOnline
   ds
   """  
   def __init__(self, obj):
      self.ipTCOnline:bool = obj["ipTCOnline"]
      """  Tax Connect status.  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class PrePostInvoices_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.gLMessage:str = obj["parameters"]
      self.gLWarning:str = obj["parameters"]
      self.collectionsWarning:str = obj["parameters"]
      self.currencyWarning:str = obj["parameters"]
      self.needsUserInput:bool = obj["needsUserInput"]
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnlockGroup_input:
   """ Required : 
   priorGroupID
   ds
   """  
   def __init__(self, obj):
      self.priorGroupID:str = obj["priorGroupID"]
      """  Prior Group ID.  """  
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class UnlockGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtInvcGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtInvcGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateForBOE_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class UpdateForBOE_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class UpdateNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

