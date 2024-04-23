import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.POScheduleSvc
# Description: POSchedule BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_POSchedules(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POSchedules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POSchedules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules",headers=creds) as resp:
           return await resp.json()

async def post_POSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POScheduleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POScheduleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev(Company, Plant, ContractPONum, ContractPOLine, ContractRev, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POSchedule item
   Description: Calls GetByID to retrieve the POSchedule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POSchedule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev(Company, Plant, ContractPONum, ContractPOLine, ContractRev, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POSchedule for the service
   Description: Calls UpdateExt to update POSchedule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POSchedule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POScheduleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev(Company, Plant, ContractPONum, ContractPOLine, ContractRev, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POSchedule item
   Description: Call UpdateExt to delete POSchedule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POSchedule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")",headers=creds) as resp:
           return await resp.json()

async def get_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev_POScheduleDtls(Company, Plant, ContractPONum, ContractPOLine, ContractRev, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get POScheduleDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_POScheduleDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")/POScheduleDtls",headers=creds) as resp:
           return await resp.json()

async def get_POSchedules_Company_Plant_ContractPONum_ContractPOLine_ContractRev_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company, Plant, ContractPONum, ContractPOLine, ContractRev, ContractPORelNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POScheduleDtl item
   Description: Calls GetByID to retrieve the POScheduleDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POScheduleDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param ContractPORelNum: Desc: ContractPORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POSchedules(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + ")/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_POScheduleDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POScheduleDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POScheduleDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls",headers=creds) as resp:
           return await resp.json()

async def post_POScheduleDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POScheduleDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company, Plant, ContractPONum, ContractPOLine, ContractRev, ContractPORelNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POScheduleDtl item
   Description: Calls GetByID to retrieve the POScheduleDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POScheduleDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param ContractPORelNum: Desc: ContractPORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company, Plant, ContractPONum, ContractPOLine, ContractRev, ContractPORelNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POScheduleDtl for the service
   Description: Calls UpdateExt to update POScheduleDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POScheduleDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param ContractPORelNum: Desc: ContractPORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POScheduleDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POScheduleDtls_Company_Plant_ContractPONum_ContractPOLine_ContractRev_ContractPORelNum(Company, Plant, ContractPONum, ContractPOLine, ContractRev, ContractPORelNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POScheduleDtl item
   Description: Call UpdateExt to delete POScheduleDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POScheduleDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ContractPONum: Desc: ContractPONum   Required: True
      :param ContractPOLine: Desc: ContractPOLine   Required: True
      :param ContractRev: Desc: ContractRev   Required: True
      :param ContractPORelNum: Desc: ContractPORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/POScheduleDtls(" + Company + "," + Plant + "," + ContractPONum + "," + ContractPOLine + "," + ContractRev + "," + ContractPORelNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POScheduleListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePOSchedule, whereClausePOScheduleDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePOSchedule=" + whereClausePOSchedule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePOScheduleDtl=" + whereClausePOScheduleDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, contractPONum, contractPOLine, contractRev, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
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
   params += "contractPONum=" + contractPONum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "contractPOLine=" + contractPOLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "contractRev=" + contractRev

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ApproveAllSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveAllSchedules
   Description: Approved all schedules
   OperationID: ApproveAllSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAllSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAllSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveMultiVendorSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveMultiVendorSchedule
   Description: Approved one schedule
   OperationID: ApproveMultiVendorSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveMultiVendorSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveMultiVendorSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveSchedule
   Description: Approved one schedule
   OperationID: ApproveSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOtherSchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOtherSchedules
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">Part number of part to check for multiple schedules </param><param name="opScheduleFound">Was another schedule foud for this part? </param>
   OperationID: CheckOtherSchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOtherSchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOtherSchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyQuantities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyQuantities
   Description: Provides a simply way of being able to copy the quantities from either the Current, Suggestion or Adjusted fields to the Proposed field for the whole schedule
   OperationID: CopyQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LastPackSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LastPackSlip
   OperationID: LastPackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LastPackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LastPackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSharedSupplierValidation(epicorHeaders = None):
   """  
   Summary: Invoke method GetSharedSupplierValidation
   Description: Purpose: GetSharedSupplierValidation
Parameters:  none
Notes:
<param name="opSharedSupplierValidation">Shared Supplier Validation? Yes/No</param>
   OperationID: GetSharedSupplierValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSharedSupplierValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetSharedSupplierValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSharedSupplierValidation
   Description: Sets a variable behind the Part Schedule Shared Supplier Validation option
   OperationID: SetSharedSupplierValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSharedSupplierValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSharedSupplierValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveAllSchedulesDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveAllSchedulesDS
   Description: Approved all schedules by data set
   OperationID: ApproveAllSchedulesDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAllSchedulesDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAllSchedulesDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOSchedule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOScheduleDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOScheduleDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOScheduleDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOScheduleDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOScheduleDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POScheduleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POScheduleDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POScheduleListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POScheduleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POScheduleRow] = obj["value"]
      pass

class Erp_Tablesets_POScheduleDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ContractRev:int = obj["ContractRev"]
      """  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  """  
      self.ContractPORelNum:int = obj["ContractPORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.LastPackSlip:str = obj["LastPackSlip"]
      """  The last Packing Slip processed for this Contract Purchase Order.  """  
      self.LastReceiptDate:str = obj["LastReceiptDate"]
      """  The Receipt Date of the last Receipt for this Contract Purchase Order.  """  
      self.LastReceiptOurQty:int = obj["LastReceiptOurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.ScheduleDate:str = obj["ScheduleDate"]
      """  Date of the current schedule, suggested demand, adjusted schedule, or proposed schedule.  """  
      self.WeekNum:int = obj["WeekNum"]
      """  The Week Number relating to the Work Date.  """  
      self.WeekYear:int = obj["WeekYear"]
      """  The Week Year relating to the Work Date.  """  
      self.CurrentOurQty:int = obj["CurrentOurQty"]
      """  Current Scheduled Quantity corresponding to a PORel.  """  
      self.SuggestedOurQty:int = obj["SuggestedOurQty"]
      """  The quantity created by the Generate PO Suggestions process.  """  
      self.AdjustedOurQty:int = obj["AdjustedOurQty"]
      """  The quantity that the Generate PO Schedules process is suggesting.  Includes a minimum quantity and is determined by the Periodicity code being used.  """  
      self.ProposedOurQty:int = obj["ProposedOurQty"]
      """  Quantity the user may propose via the Purchase Order Contract Schedule Maintenance.  """  
      self.OurQtyUOM:str = obj["OurQtyUOM"]
      """  Inventory UOM  """  
      self.POSuggLastPackSlip:str = obj["POSuggLastPackSlip"]
      """  The last packing slip number that a receipt was made against this Purchase Order Contract at the time Generate Purchase Suggestions was run.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdjustedOurQtyDisp:int = obj["AdjustedOurQtyDisp"]
      """  Adjusted Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.CurrentOurQtyDisp:int = obj["CurrentOurQtyDisp"]
      """  Current Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.ProposedOurQtyDisp:int = obj["ProposedOurQtyDisp"]
      """  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.SuggestedOurQtyDisp:int = obj["SuggestedOurQtyDisp"]
      """  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory UOM for the Part  """  
      self.ReceivedOurQtyDisp:int = obj["ReceivedOurQtyDisp"]
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.PODetailPartNum:str = obj["PODetailPartNum"]
      self.PODetailPUM:str = obj["PODetailPUM"]
      self.PORelReceivedQty:int = obj["PORelReceivedQty"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POScheduleListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ContractRev:int = obj["ContractRev"]
      """  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date the Purchase Order Schedule was created.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Purchase Order Schedule was approved.  """  
      self.PrintedDate:str = obj["PrintedDate"]
      """  Date the Purchase Order Schedule was printed.  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  Date the Purchase Order Schedule was last executed.  """  
      self.ActiveRevision:bool = obj["ActiveRevision"]
      """  Is this Revision of the Purchase Order Schedule active?  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number for this Purchase Order Contract Schedule.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number for this Purchase Order Contract Schedule.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  POHeader.ContractEndDate  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  POHeader.ContractStartDate  """  
      self.ContractQty:int = obj["ContractQty"]
      """  PODetail.ContractQty  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part.PartDescription  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.PurPoint:str = obj["PurPoint"]
      """  POHeader.PurPoint  """  
      self.POSuggLastPackSlip:str = obj["POSuggLastPackSlip"]
      self.LastPackSlip:str = obj["LastPackSlip"]
      self.LastReceiptDate:str = obj["LastReceiptDate"]
      self.LastReceiptOurQty:int = obj["LastReceiptOurQty"]
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  PODetail.ContractQtyUOM  """  
      self.LastReceiptOurQtyUOM:str = obj["LastReceiptOurQtyUOM"]
      """  Last Receipt UOM  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      self.ReductionMethod:int = obj["ReductionMethod"]
      self.TotalArrivedQuantity:int = obj["TotalArrivedQuantity"]
      """  The sum of PORel.ArrivedQty for the current PO Line  """  
      self.TotalReceiptQuantity:int = obj["TotalReceiptQuantity"]
      """  The sum of PORel.Received for the current PO Line  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartIUM:str = obj["PartIUM"]
      self.PlantName:str = obj["PlantName"]
      self.PODetailContractQty:int = obj["PODetailContractQty"]
      self.PODetailContractQtyUOM:str = obj["PODetailContractQtyUOM"]
      self.PODetailOrderQty:int = obj["PODetailOrderQty"]
      self.POHeaderPurPoint:str = obj["POHeaderPurPoint"]
      self.POHeaderContractEndDate:str = obj["POHeaderContractEndDate"]
      self.POHeaderContractStartDate:str = obj["POHeaderContractStartDate"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName_:str = obj["VendorName_"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POScheduleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ContractRev:int = obj["ContractRev"]
      """  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date the Purchase Order Schedule was created.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Purchase Order Schedule was approved.  """  
      self.PrintedDate:str = obj["PrintedDate"]
      """  Date the Purchase Order Schedule was printed.  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  Date the Purchase Order Schedule was last executed.  """  
      self.ActiveRevision:bool = obj["ActiveRevision"]
      """  Is this Revision of the Purchase Order Schedule active?  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number for this Purchase Order Contract Schedule.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number for this Purchase Order Contract Schedule.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractQty:int = obj["ContractQty"]
      """  PODetail.ContractQty  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part.PartDescription  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.PurPoint:str = obj["PurPoint"]
      """  POHeader.PurPoint  """  
      self.POSuggLastPackSlip:str = obj["POSuggLastPackSlip"]
      self.LastPackSlip:str = obj["LastPackSlip"]
      self.LastReceiptDate:str = obj["LastReceiptDate"]
      self.LastReceiptOurQty:int = obj["LastReceiptOurQty"]
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  PODetail.ContractQtyUOM  """  
      self.LastReceiptOurQtyUOM:str = obj["LastReceiptOurQtyUOM"]
      """  Last Receipt UOM  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      self.ReductionMethod:int = obj["ReductionMethod"]
      self.TotalArrivedQuantity:int = obj["TotalArrivedQuantity"]
      """  The sum of PORel.ArrivedQty for the current PO Line  """  
      self.TotalReceiptQuantity:int = obj["TotalReceiptQuantity"]
      """  The sum of PORel.Received for the current PO Line  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PODetailContractQty:int = obj["PODetailContractQty"]
      self.PODetailContractQtyUOM:str = obj["PODetailContractQtyUOM"]
      self.PODetailOrderQty:int = obj["PODetailOrderQty"]
      self.POHeaderContractStartDate:str = obj["POHeaderContractStartDate"]
      self.POHeaderPurPoint:str = obj["POHeaderPurPoint"]
      self.POHeaderContractEndDate:str = obj["POHeaderContractEndDate"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName_:str = obj["VendorName_"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApproveAllSchedulesDS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

class ApproveAllSchedulesDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ApproveAllSchedules_input:
   """ Required : 
   poScheduleIDList
   reductionMethodList
   """  
   def __init__(self, obj):
      self.poScheduleIDList:str = obj["poScheduleIDList"]
      """  A Guid array carrying all PO Schedule Row IDs to be approved  """  
      self.reductionMethodList:int = obj["reductionMethodList"]
      """  An int array carrying PO Schedules Reduction Method  """  
      pass

class ApproveAllSchedules_output:
   def __init__(self, obj):
      pass

class ApproveMultiVendorSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

class ApproveMultiVendorSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ApproveSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

class ApproveSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckOtherSchedules_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class CheckOtherSchedules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opScheduleFound:bool = obj["opScheduleFound"]
      pass

      """  output parameters  """  

class CopyQuantities_input:
   """ Required : 
   ipFromField
   ipPlant
   ipContractPONum
   ipContractPOLine
   ipContractRev
   ds
   """  
   def __init__(self, obj):
      self.ipFromField:str = obj["ipFromField"]
      """  The From field value  """  
      self.ipPlant:str = obj["ipPlant"]
      """  The current Plant value  """  
      self.ipContractPONum:int = obj["ipContractPONum"]
      """  The current ContractPONum value  """  
      self.ipContractPOLine:int = obj["ipContractPOLine"]
      """  The current ContractPOLine value  """  
      self.ipContractRev:int = obj["ipContractRev"]
      """  The current ContractRev value  """  
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

class CopyQuantities_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   plant
   contractPONum
   contractPOLine
   contractRev
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.contractPONum:int = obj["contractPONum"]
      self.contractPOLine:int = obj["contractPOLine"]
      self.contractRev:int = obj["contractRev"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_POScheduleDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ContractRev:int = obj["ContractRev"]
      """  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  """  
      self.ContractPORelNum:int = obj["ContractPORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.LastPackSlip:str = obj["LastPackSlip"]
      """  The last Packing Slip processed for this Contract Purchase Order.  """  
      self.LastReceiptDate:str = obj["LastReceiptDate"]
      """  The Receipt Date of the last Receipt for this Contract Purchase Order.  """  
      self.LastReceiptOurQty:int = obj["LastReceiptOurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.ScheduleDate:str = obj["ScheduleDate"]
      """  Date of the current schedule, suggested demand, adjusted schedule, or proposed schedule.  """  
      self.WeekNum:int = obj["WeekNum"]
      """  The Week Number relating to the Work Date.  """  
      self.WeekYear:int = obj["WeekYear"]
      """  The Week Year relating to the Work Date.  """  
      self.CurrentOurQty:int = obj["CurrentOurQty"]
      """  Current Scheduled Quantity corresponding to a PORel.  """  
      self.SuggestedOurQty:int = obj["SuggestedOurQty"]
      """  The quantity created by the Generate PO Suggestions process.  """  
      self.AdjustedOurQty:int = obj["AdjustedOurQty"]
      """  The quantity that the Generate PO Schedules process is suggesting.  Includes a minimum quantity and is determined by the Periodicity code being used.  """  
      self.ProposedOurQty:int = obj["ProposedOurQty"]
      """  Quantity the user may propose via the Purchase Order Contract Schedule Maintenance.  """  
      self.OurQtyUOM:str = obj["OurQtyUOM"]
      """  Inventory UOM  """  
      self.POSuggLastPackSlip:str = obj["POSuggLastPackSlip"]
      """  The last packing slip number that a receipt was made against this Purchase Order Contract at the time Generate Purchase Suggestions was run.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.

Formula: XRelQty * Factor = RelQty  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdjustedOurQtyDisp:int = obj["AdjustedOurQtyDisp"]
      """  Adjusted Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.CurrentOurQtyDisp:int = obj["CurrentOurQtyDisp"]
      """  Current Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.ProposedOurQtyDisp:int = obj["ProposedOurQtyDisp"]
      """  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.SuggestedOurQtyDisp:int = obj["SuggestedOurQtyDisp"]
      """  Proposed Our Qty displayed in terms of the Primary UOM of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory UOM for the Part  """  
      self.ReceivedOurQtyDisp:int = obj["ReceivedOurQtyDisp"]
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.PODetailPartNum:str = obj["PODetailPartNum"]
      self.PODetailPUM:str = obj["PODetailPUM"]
      self.PORelReceivedQty:int = obj["PORelReceivedQty"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POScheduleListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ContractRev:int = obj["ContractRev"]
      """  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date the Purchase Order Schedule was created.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Purchase Order Schedule was approved.  """  
      self.PrintedDate:str = obj["PrintedDate"]
      """  Date the Purchase Order Schedule was printed.  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  Date the Purchase Order Schedule was last executed.  """  
      self.ActiveRevision:bool = obj["ActiveRevision"]
      """  Is this Revision of the Purchase Order Schedule active?  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number for this Purchase Order Contract Schedule.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number for this Purchase Order Contract Schedule.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractEndDate:str = obj["ContractEndDate"]
      """  POHeader.ContractEndDate  """  
      self.ContractStartDate:str = obj["ContractStartDate"]
      """  POHeader.ContractStartDate  """  
      self.ContractQty:int = obj["ContractQty"]
      """  PODetail.ContractQty  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part.PartDescription  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.PurPoint:str = obj["PurPoint"]
      """  POHeader.PurPoint  """  
      self.POSuggLastPackSlip:str = obj["POSuggLastPackSlip"]
      self.LastPackSlip:str = obj["LastPackSlip"]
      self.LastReceiptDate:str = obj["LastReceiptDate"]
      self.LastReceiptOurQty:int = obj["LastReceiptOurQty"]
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  PODetail.ContractQtyUOM  """  
      self.LastReceiptOurQtyUOM:str = obj["LastReceiptOurQtyUOM"]
      """  Last Receipt UOM  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      self.ReductionMethod:int = obj["ReductionMethod"]
      self.TotalArrivedQuantity:int = obj["TotalArrivedQuantity"]
      """  The sum of PORel.ArrivedQty for the current PO Line  """  
      self.TotalReceiptQuantity:int = obj["TotalReceiptQuantity"]
      """  The sum of PORel.Received for the current PO Line  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartIUM:str = obj["PartIUM"]
      self.PlantName:str = obj["PlantName"]
      self.PODetailContractQty:int = obj["PODetailContractQty"]
      self.PODetailContractQtyUOM:str = obj["PODetailContractQtyUOM"]
      self.PODetailOrderQty:int = obj["PODetailOrderQty"]
      self.POHeaderPurPoint:str = obj["POHeaderPurPoint"]
      self.POHeaderContractEndDate:str = obj["POHeaderContractEndDate"]
      self.POHeaderContractStartDate:str = obj["POHeaderContractStartDate"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName_:str = obj["VendorName_"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POScheduleListTableset:
   def __init__(self, obj):
      self.POScheduleList:list[Erp_Tablesets_POScheduleListRow] = obj["POScheduleList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POScheduleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ContractPONum:int = obj["ContractPONum"]
      """  Purchase order number that uniquely identifies the Contract Purchase Order.  """  
      self.ContractPOLine:int = obj["ContractPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Contract Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ContractRev:int = obj["ContractRev"]
      """  Contract Sequence Number used to uniquely identify this revision of the Purchase Order Contract.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date the Purchase Order Schedule was created.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the Purchase Order Schedule was approved.  """  
      self.PrintedDate:str = obj["PrintedDate"]
      """  Date the Purchase Order Schedule was printed.  """  
      self.LastRunDate:str = obj["LastRunDate"]
      """  Date the Purchase Order Schedule was last executed.  """  
      self.ActiveRevision:bool = obj["ActiveRevision"]
      """  Is this Revision of the Purchase Order Schedule active?  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number for this Purchase Order Contract Schedule.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number for this Purchase Order Contract Schedule.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The ID that links to the Purchasing Agent master file.  """  
      self.DevChar01:str = obj["DevChar01"]
      """  For development use only.  """  
      self.DevChar02:str = obj["DevChar02"]
      """  For development use only.  """  
      self.DevChar03:str = obj["DevChar03"]
      """  For development use only.  """  
      self.DevChar04:str = obj["DevChar04"]
      """  For development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractQty:int = obj["ContractQty"]
      """  PODetail.ContractQty  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part.PartDescription  """  
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.PurPoint:str = obj["PurPoint"]
      """  POHeader.PurPoint  """  
      self.POSuggLastPackSlip:str = obj["POSuggLastPackSlip"]
      self.LastPackSlip:str = obj["LastPackSlip"]
      self.LastReceiptDate:str = obj["LastReceiptDate"]
      self.LastReceiptOurQty:int = obj["LastReceiptOurQty"]
      self.ContractQtyUOM:str = obj["ContractQtyUOM"]
      """  PODetail.ContractQtyUOM  """  
      self.LastReceiptOurQtyUOM:str = obj["LastReceiptOurQtyUOM"]
      """  Last Receipt UOM  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      self.ReductionMethod:int = obj["ReductionMethod"]
      self.TotalArrivedQuantity:int = obj["TotalArrivedQuantity"]
      """  The sum of PORel.ArrivedQty for the current PO Line  """  
      self.TotalReceiptQuantity:int = obj["TotalReceiptQuantity"]
      """  The sum of PORel.Received for the current PO Line  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PODetailContractQty:int = obj["PODetailContractQty"]
      self.PODetailContractQtyUOM:str = obj["PODetailContractQtyUOM"]
      self.PODetailOrderQty:int = obj["PODetailOrderQty"]
      self.POHeaderContractStartDate:str = obj["POHeaderContractStartDate"]
      self.POHeaderPurPoint:str = obj["POHeaderPurPoint"]
      self.POHeaderContractEndDate:str = obj["POHeaderContractEndDate"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName_:str = obj["VendorName_"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POScheduleTableset:
   def __init__(self, obj):
      self.POSchedule:list[Erp_Tablesets_POScheduleRow] = obj["POSchedule"]
      self.POScheduleDtl:list[Erp_Tablesets_POScheduleDtlRow] = obj["POScheduleDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPOScheduleTableset:
   def __init__(self, obj):
      self.POSchedule:list[Erp_Tablesets_POScheduleRow] = obj["POSchedule"]
      self.POScheduleDtl:list[Erp_Tablesets_POScheduleDtlRow] = obj["POScheduleDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   contractPONum
   contractPOLine
   contractRev
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.contractPONum:int = obj["contractPONum"]
      self.contractPOLine:int = obj["contractPOLine"]
      self.contractRev:int = obj["contractRev"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POScheduleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POScheduleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POScheduleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POScheduleListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPOScheduleDtl_input:
   """ Required : 
   ds
   plant
   contractPONum
   contractPOLine
   contractRev
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.contractPONum:int = obj["contractPONum"]
      self.contractPOLine:int = obj["contractPOLine"]
      self.contractRev:int = obj["contractRev"]
      pass

class GetNewPOScheduleDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPOSchedule_input:
   """ Required : 
   ds
   plant
   contractPONum
   contractPOLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.contractPONum:int = obj["contractPONum"]
      self.contractPOLine:int = obj["contractPOLine"]
      pass

class GetNewPOSchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePOSchedule
   whereClausePOScheduleDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOSchedule:str = obj["whereClausePOSchedule"]
      self.whereClausePOScheduleDtl:str = obj["whereClausePOScheduleDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POScheduleTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSharedSupplierValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opSharedSupplierValidation:bool = obj["opSharedSupplierValidation"]
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

class LastPackSlip_input:
   """ Required : 
   ipPONum
   ipPOLine
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      self.ipPOLine:int = obj["ipPOLine"]
      pass

class LastPackSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPackSlip:str = obj["parameters"]
      self.opReceiptDate:str = obj["parameters"]
      self.opReceiptOurQty:int = obj["parameters"]
      self.opReceiptOurQtyUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetSharedSupplierValidation_input:
   """ Required : 
   ipSharedSupplierValidation
   """  
   def __init__(self, obj):
      self.ipSharedSupplierValidation:bool = obj["ipSharedSupplierValidation"]
      """  True or False  """  
      pass

class SetSharedSupplierValidation_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOScheduleTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOScheduleTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POScheduleTableset] = obj["ds"]
      pass

      """  output parameters  """  

