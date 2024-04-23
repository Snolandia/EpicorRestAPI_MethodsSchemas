import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlConfigSvc
# Description: PkgControlConfigSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlConfigs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlConfigs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlConfigs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlConfigs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlConfigs_Company_Plant_PkgControlIDCode(Company, Plant, PkgControlIDCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlConfig item
   Description: Calls GetByID to retrieve the PkgControlConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlConfigs_Company_Plant_PkgControlIDCode(Company, Plant, PkgControlIDCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlConfig for the service
   Description: Calls UpdateExt to update PkgControlConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlConfigs_Company_Plant_PkgControlIDCode(Company, Plant, PkgControlIDCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlConfig item
   Description: Call UpdateExt to delete PkgControlConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlConfigs_Company_Plant_PkgControlIDCode_PkgControlSegments(Company, Plant, PkgControlIDCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PkgControlSegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlSegments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")/PkgControlSegments",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlConfigs_Company_Plant_PkgControlIDCode_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company, Plant, PkgControlIDCode, SegmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlSegment item
   Description: Calls GetByID to retrieve the PkgControlSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlSegment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlConfigs(" + Company + "," + Plant + "," + PkgControlIDCode + ")/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlSegments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlSegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlSegments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlSegments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company, Plant, PkgControlIDCode, SegmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlSegment item
   Description: Calls GetByID to retrieve the PkgControlSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company, Plant, PkgControlIDCode, SegmentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlSegment for the service
   Description: Calls UpdateExt to update PkgControlSegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlSegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlSegments_Company_Plant_PkgControlIDCode_SegmentNum(Company, Plant, PkgControlIDCode, SegmentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlSegment item
   Description: Call UpdateExt to delete PkgControlSegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/PkgControlSegments(" + Company + "," + Plant + "," + PkgControlIDCode + "," + SegmentNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePkgControl, whereClausePkgControlSegment, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePkgControl=" + whereClausePkgControl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlSegment=" + whereClausePkgControlSegment
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, pkgControlIDCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pkgControlIDCode=" + pkgControlIDCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_InitializeStaticPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitializeStaticPCID
   Description: Initializes a Static PCID if it does not already exist.
   OperationID: InitializeStaticPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeStaticPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeStaticPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitializeDynamicPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitializeDynamicPCID
   Description: Initializes a Dynamic PCID if it does not already exist.
   OperationID: InitializeDynamicPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeDynamicPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeDynamicPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeActive
   Description: This method performs validation for active flag
   OperationID: OnChangeActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAllowVoid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAllowVoid
   Description: This method resets default values when AllowVoid changes
   OperationID: OnChangeAllowVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllowVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllowVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeControlIDCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeControlIDCode
   Description: Update Control ID information when the Control ID Code is changed.
   OperationID: OnChangeControlIDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePkgCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePkgCode
   Description: Update Package Code information when the Package Code is changed.
   OperationID: OnChangePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PkgControlPreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PkgControlPreUpdate
   Description: Called before update - checks to see if PCID has already been initialized with different settings.
Warning if static PCID / flags changed / in use
   OperationID: PkgControlPreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PkgControlPreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PkgControlPreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintPCID
   Description: Print PCID
   OperationID: PrintPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List from Service Designer.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePkgControlIDCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePkgControlIDCode
   OperationID: OnChangePkgControlIDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePkgControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePkgControlType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePkgControlType
   OperationID: OnChangePkgControlType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePkgControlType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgControlType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateStaticEmptyBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateStaticEmptyBinNum
   Description: Validates if a given Bin is valid for the given Warehouse.
   OperationID: ValidateStaticEmptyBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateStaticEmptyBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStaticEmptyBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateStaticEmptyWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateStaticEmptyWarehouseCode
   Description: Validates if a given Warehouse is valid.
   OperationID: ValidateStaticEmptyWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateStaticEmptyWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateStaticEmptyWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlSegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlSegmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlSegmentRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.PkgControlIDDesc:str = obj["PkgControlIDDesc"]
      """  Package Control ID Description.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.PkgControlIDDesc:str = obj["PkgControlIDDesc"]
      """  Package Control ID Description.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM and Part Quantity per child PCID. This is referred to as a Master PCID otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMultipleSerialNumsPerPCID:bool = obj["AllowMultipleSerialNumsPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoid:bool = obj["AllowVoid"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDelete:bool = obj["AllowDelete"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InitializationHasOccurred:bool = obj["InitializationHasOccurred"]
      """  Indicates of an Initialization of a PCID has occurred using this Package Control ID Configuration.  The value is false when an initialization has not occurred to indicate last value fields do not hold a true last value.  Once an initialization has occurred, last value fields contain ongoing values to be used for incrementing.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  Indicates if the package control ID is an outbound container.  """  
      self.DefaultForStatic:bool = obj["DefaultForStatic"]
      """  DefaultForStatic  """  
      self.DefaultForDynamic:bool = obj["DefaultForDynamic"]
      """  DefaultForDynamic  """  
      self.StaticEmptyWarehouseCode:str = obj["StaticEmptyWarehouseCode"]
      """  Warehouse where a Static PCID will be stored when emptied.  """  
      self.StaticEmptyBinNum:str = obj["StaticEmptyBinNum"]
      """  Bin where a Static PCID will be stored when emptied.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.DisableControlIDCode:bool = obj["DisableControlIDCode"]
      """  If true, disable ControlIDCode.  If false, enable ControlIDCode  """  
      self.ExampleIDValue:str = obj["ExampleIDValue"]
      """  Package Control ID example.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if the Package Control ID has been used.  Default is false.  """  
      self.RangeFrom:str = obj["RangeFrom"]
      """  Package Control ID starting range.  """  
      self.RangeTo:str = obj["RangeTo"]
      """  Package Control ID ending range.  """  
      self.Reinitialize:bool = obj["Reinitialize"]
      self.CharactersUsed:int = obj["CharactersUsed"]
      """  The number of characters used in the Package Control ID.  """  
      self.DefinedSegments:int = obj["DefinedSegments"]
      """  The number of segments defined and associated with the Package Control ID.  """  
      self.StaticEmptyBinDesc:str = obj["StaticEmptyBinDesc"]
      """  Static Empty Bin Description  """  
      self.StaticEmptyWarehouseDesc:str = obj["StaticEmptyWarehouseDesc"]
      """  Empty Static Warehouse Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ControlIDControlIDDesc:str = obj["ControlIDControlIDDesc"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlSegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.SegmentNum:int = obj["SegmentNum"]
      """  Unique Segment Number within the Control ID Code.  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment Description.  """  
      self.AlphaRangeFrom:str = obj["AlphaRangeFrom"]
      """  Segment starting string of the alphanumeric range based on segment format.  """  
      self.AlphaRangeTo:str = obj["AlphaRangeTo"]
      """  Segment ending string of the alphanumeric range based on segment format.  """  
      self.AlphaRangeLastValue:str = obj["AlphaRangeLastValue"]
      """  Segment last value string of the alphanumeric range based on segment format.  """  
      self.NumericRangeFrom:int = obj["NumericRangeFrom"]
      """  Segment starting value of the numeric range based on segment format.  """  
      self.NumericRangeTo:int = obj["NumericRangeTo"]
      """  Segment ending value of the numeric range based on segment format.  """  
      self.NumericRangeLastValue:int = obj["NumericRangeLastValue"]
      """  Segment last value of the numeric range based on segment format.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SegmentPosition:int = obj["SegmentPosition"]
      """  Segment Position within the Control ID.  """  
      self.SegmentType:str = obj["SegmentType"]
      """  Segment Type.  Valid values are AlphaSequential, NumericSequential, DateNumericSequential, Date, and Fixed.  There can be an unlimited number of Fixed segments, only one segment of each other type may exist within the Control ID.  DateNumericSequential may only exist if a Date segment exists.  """  
      self.SegmentFormat:str = obj["SegmentFormat"]
      """  Segment format as input by the user. Valid values are "&" for AlphaNumeric segments, "@" for Alpha Only segments, "#" for Numeric Only segments.  For date segments, "<D>" represents a 2 digit day, "<M>" represents a 2 digit month, "<YY>" represents a 2 digit year, "<YYYY>" represents a 4 digit year, "<TJD>" represents a 5 digit Truncated Julian Date, and "<T>" represents time in a 6 digit integer.  Valid values for Fixed segments are "a-z", "A-Z", "0-9", "-"  """  
      self.RolloverTrigger:str = obj["RolloverTrigger"]
      """  Based on the segment type:  If segment type is Sequential, value is Sequential.  If segment type is Fixed, value is Fixed.  """  
      self.RolloverAction:str = obj["RolloverAction"]
      """  Indicates the action to be taken when the Control ID reaches its limit.  Valid values vary per Rollover Trigger.  If rollover trigger is Sequential or DateNumericSequential, valid values are Stop and Range From.  If rollover trigger is Fixed or Date, valid value is blank.  """  
      self.DateLastValue:str = obj["DateLastValue"]
      """  Segment last value of the date based on segment format.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Indicates if the segment is of a fixed length.  """  
      self.ExampleIDValue:str = obj["ExampleIDValue"]
      self.NumericRangeStartingAt:int = obj["NumericRangeStartingAt"]
      """  Starting at value - used to initialize the last value for newly created configurations  """  
      self.AlphaRangeStartingAt:str = obj["AlphaRangeStartingAt"]
      """  Starting at value - used to initialize the last value for newly created configurations  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ControlIDControlIDDesc:str = obj["ControlIDControlIDDesc"]
      self.PkgControlPkgControlIDDesc:str = obj["PkgControlPkgControlIDDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PkgControlConfigListTableset:
   def __init__(self, obj):
      self.PkgControlList:list[Erp_Tablesets_PkgControlListRow] = obj["PkgControlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlConfigTableset:
   def __init__(self, obj):
      self.PkgControl:list[Erp_Tablesets_PkgControlRow] = obj["PkgControl"]
      self.PkgControlSegment:list[Erp_Tablesets_PkgControlSegmentRow] = obj["PkgControlSegment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.PkgControlIDDesc:str = obj["PkgControlIDDesc"]
      """  Package Control ID Description.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.PkgControlIDDesc:str = obj["PkgControlIDDesc"]
      """  Package Control ID Description.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM and Part Quantity per child PCID. This is referred to as a Master PCID otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMultipleSerialNumsPerPCID:bool = obj["AllowMultipleSerialNumsPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoid:bool = obj["AllowVoid"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDelete:bool = obj["AllowDelete"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InitializationHasOccurred:bool = obj["InitializationHasOccurred"]
      """  Indicates of an Initialization of a PCID has occurred using this Package Control ID Configuration.  The value is false when an initialization has not occurred to indicate last value fields do not hold a true last value.  Once an initialization has occurred, last value fields contain ongoing values to be used for incrementing.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  Indicates if the package control ID is an outbound container.  """  
      self.DefaultForStatic:bool = obj["DefaultForStatic"]
      """  DefaultForStatic  """  
      self.DefaultForDynamic:bool = obj["DefaultForDynamic"]
      """  DefaultForDynamic  """  
      self.StaticEmptyWarehouseCode:str = obj["StaticEmptyWarehouseCode"]
      """  Warehouse where a Static PCID will be stored when emptied.  """  
      self.StaticEmptyBinNum:str = obj["StaticEmptyBinNum"]
      """  Bin where a Static PCID will be stored when emptied.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.DisableControlIDCode:bool = obj["DisableControlIDCode"]
      """  If true, disable ControlIDCode.  If false, enable ControlIDCode  """  
      self.ExampleIDValue:str = obj["ExampleIDValue"]
      """  Package Control ID example.  """  
      self.InUse:bool = obj["InUse"]
      """  Indicates if the Package Control ID has been used.  Default is false.  """  
      self.RangeFrom:str = obj["RangeFrom"]
      """  Package Control ID starting range.  """  
      self.RangeTo:str = obj["RangeTo"]
      """  Package Control ID ending range.  """  
      self.Reinitialize:bool = obj["Reinitialize"]
      self.CharactersUsed:int = obj["CharactersUsed"]
      """  The number of characters used in the Package Control ID.  """  
      self.DefinedSegments:int = obj["DefinedSegments"]
      """  The number of segments defined and associated with the Package Control ID.  """  
      self.StaticEmptyBinDesc:str = obj["StaticEmptyBinDesc"]
      """  Static Empty Bin Description  """  
      self.StaticEmptyWarehouseDesc:str = obj["StaticEmptyWarehouseDesc"]
      """  Empty Static Warehouse Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ControlIDControlIDDesc:str = obj["ControlIDControlIDDesc"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlSegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ControlIDCode:str = obj["ControlIDCode"]
      """  Unique code assigned by the user for this Control ID.  """  
      self.SegmentNum:int = obj["SegmentNum"]
      """  Unique Segment Number within the Control ID Code.  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment Description.  """  
      self.AlphaRangeFrom:str = obj["AlphaRangeFrom"]
      """  Segment starting string of the alphanumeric range based on segment format.  """  
      self.AlphaRangeTo:str = obj["AlphaRangeTo"]
      """  Segment ending string of the alphanumeric range based on segment format.  """  
      self.AlphaRangeLastValue:str = obj["AlphaRangeLastValue"]
      """  Segment last value string of the alphanumeric range based on segment format.  """  
      self.NumericRangeFrom:int = obj["NumericRangeFrom"]
      """  Segment starting value of the numeric range based on segment format.  """  
      self.NumericRangeTo:int = obj["NumericRangeTo"]
      """  Segment ending value of the numeric range based on segment format.  """  
      self.NumericRangeLastValue:int = obj["NumericRangeLastValue"]
      """  Segment last value of the numeric range based on segment format.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SegmentPosition:int = obj["SegmentPosition"]
      """  Segment Position within the Control ID.  """  
      self.SegmentType:str = obj["SegmentType"]
      """  Segment Type.  Valid values are AlphaSequential, NumericSequential, DateNumericSequential, Date, and Fixed.  There can be an unlimited number of Fixed segments, only one segment of each other type may exist within the Control ID.  DateNumericSequential may only exist if a Date segment exists.  """  
      self.SegmentFormat:str = obj["SegmentFormat"]
      """  Segment format as input by the user. Valid values are "&" for AlphaNumeric segments, "@" for Alpha Only segments, "#" for Numeric Only segments.  For date segments, "<D>" represents a 2 digit day, "<M>" represents a 2 digit month, "<YY>" represents a 2 digit year, "<YYYY>" represents a 4 digit year, "<TJD>" represents a 5 digit Truncated Julian Date, and "<T>" represents time in a 6 digit integer.  Valid values for Fixed segments are "a-z", "A-Z", "0-9", "-"  """  
      self.RolloverTrigger:str = obj["RolloverTrigger"]
      """  Based on the segment type:  If segment type is Sequential, value is Sequential.  If segment type is Fixed, value is Fixed.  """  
      self.RolloverAction:str = obj["RolloverAction"]
      """  Indicates the action to be taken when the Control ID reaches its limit.  Valid values vary per Rollover Trigger.  If rollover trigger is Sequential or DateNumericSequential, valid values are Stop and Range From.  If rollover trigger is Fixed or Date, valid value is blank.  """  
      self.DateLastValue:str = obj["DateLastValue"]
      """  Segment last value of the date based on segment format.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Indicates if the segment is of a fixed length.  """  
      self.ExampleIDValue:str = obj["ExampleIDValue"]
      self.NumericRangeStartingAt:int = obj["NumericRangeStartingAt"]
      """  Starting at value - used to initialize the last value for newly created configurations  """  
      self.AlphaRangeStartingAt:str = obj["AlphaRangeStartingAt"]
      """  Starting at value - used to initialize the last value for newly created configurations  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ControlIDControlIDDesc:str = obj["ControlIDControlIDDesc"]
      self.PkgControlPkgControlIDDesc:str = obj["PkgControlPkgControlIDDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPkgControlConfigTableset:
   def __init__(self, obj):
      self.PkgControl:list[Erp_Tablesets_PkgControlRow] = obj["PkgControl"]
      self.PkgControlSegment:list[Erp_Tablesets_PkgControlSegmentRow] = obj["PkgControlSegment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlConfigTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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
      self.returnObj:list[Erp_Tablesets_PkgControlConfigListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPkgControlSegment_input:
   """ Required : 
   ds
   plant
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      pass

class GetNewPkgControlSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPkgControl_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewPkgControl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePkgControl
   whereClausePkgControlSegment
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePkgControl:str = obj["whereClausePkgControl"]
      self.whereClausePkgControlSegment:str = obj["whereClausePkgControlSegment"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlConfigTableset] = obj["returnObj"]
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

class InitializeDynamicPCID_input:
   """ Required : 
   ipCompany
   ipPlant
   ipPkgControlIDCode
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  Current Company  """  
      self.ipPlant:str = obj["ipPlant"]
      """  Current Site  """  
      self.ipPkgControlIDCode:str = obj["ipPkgControlIDCode"]
      """  Package Control ID Code  """  
      pass

class InitializeDynamicPCID_output:
   def __init__(self, obj):
      pass

class InitializeStaticPCID_input:
   """ Required : 
   ipCompany
   ipPlant
   ipPkgControlIDCode
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  Current Company  """  
      self.ipPlant:str = obj["ipPlant"]
      """  Current Site  """  
      self.ipPkgControlIDCode:str = obj["ipPkgControlIDCode"]
      """  Package Control ID Code  """  
      pass

class InitializeStaticPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.PCID:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeActive_input:
   """ Required : 
   activeFlag
   ds
   """  
   def __init__(self, obj):
      self.activeFlag:bool = obj["activeFlag"]
      """  Proposed active value  """  
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class OnChangeActive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAllowVoid_input:
   """ Required : 
   ipAllowVoid
   ds
   """  
   def __init__(self, obj):
      self.ipAllowVoid:bool = obj["ipAllowVoid"]
      """  Proposed AllowVoid field  """  
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class OnChangeAllowVoid_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeControlIDCode_input:
   """ Required : 
   ipControlIDCode
   ds
   """  
   def __init__(self, obj):
      self.ipControlIDCode:str = obj["ipControlIDCode"]
      """  The Control ID Code  """  
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class OnChangeControlIDCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePkgCode_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      """  The Package Code  """  
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class OnChangePkgCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePkgControlIDCode_input:
   """ Required : 
   proposedPkgControlIDCode
   ds
   """  
   def __init__(self, obj):
      self.proposedPkgControlIDCode:str = obj["proposedPkgControlIDCode"]
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class OnChangePkgControlIDCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePkgControlType_input:
   """ Required : 
   proposedPkgControlType
   ds
   """  
   def __init__(self, obj):
      self.proposedPkgControlType:str = obj["proposedPkgControlType"]
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class OnChangePkgControlType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PkgControlPreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class PkgControlPreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrintPCID_input:
   """ Required : 
   ipPCID
   ipPrinterID
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  PCID  """  
      self.ipPrinterID:str = obj["ipPrinterID"]
      """  Printer ID  """  
      pass

class PrintPCID_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlConfigTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlConfigTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateStaticEmptyBinNum_input:
   """ Required : 
   warehouseCode
   binNum
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      pass

class ValidateStaticEmptyBinNum_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateStaticEmptyWarehouseCode_input:
   """ Required : 
   warehouseCode
   currentPlantID
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      self.currentPlantID:str = obj["currentPlantID"]
      pass

class ValidateStaticEmptyWarehouseCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

