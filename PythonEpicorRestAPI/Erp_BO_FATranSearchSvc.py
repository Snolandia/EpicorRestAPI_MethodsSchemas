import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FATranSearchSvc
# Description: FATran records for Asset Tracker
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FATranSearches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FATranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FATranSearches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches",headers=creds) as resp:
           return await resp.json()

async def post_FATranSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FATranSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAScheduleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAScheduleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FATranSearches_Company_AssetNum_AssetRegID_DetailNum(Company, AssetNum, AssetRegID, DetailNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FATranSearch item
   Description: Calls GetByID to retrieve the FATranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FATranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAScheduleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FATranSearches_Company_AssetNum_AssetRegID_DetailNum(Company, AssetNum, AssetRegID, DetailNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FATranSearch for the service
   Description: Calls UpdateExt to update FATranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FATranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAScheduleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FATranSearches_Company_AssetNum_AssetRegID_DetailNum(Company, AssetNum, AssetRegID, DetailNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FATranSearch item
   Description: Call UpdateExt to delete FATranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FATranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FATranSearches_Company_AssetNum_AssetRegID_DetailNum_FATrans(Company, AssetNum, AssetRegID, DetailNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FATrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FATrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FATranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")/FATrans",headers=creds) as resp:
           return await resp.json()

async def get_FATranSearches_Company_AssetNum_AssetRegID_DetailNum_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company, AssetNum, AssetRegID, DetailNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FATran item
   Description: Calls GetByID to retrieve the FATran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FATran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FATranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FATrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FATrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FATrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FATranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans",headers=creds) as resp:
           return await resp.json()

async def post_FATrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FATrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FATranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FATranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company, AssetNum, AssetRegID, DetailNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FATran item
   Description: Calls GetByID to retrieve the FATran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FATran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FATranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company, AssetNum, AssetRegID, DetailNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FATran for the service
   Description: Calls UpdateExt to update FATran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FATran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FATranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company, AssetNum, AssetRegID, DetailNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FATran item
   Description: Call UpdateExt to delete FATran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FATran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DetailNum: Desc: DetailNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAScheduleListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFASchedule, whereClauseFATran, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFASchedule=" + whereClauseFASchedule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFATran=" + whereClauseFATran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, assetRegID, detailNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "assetNum=" + assetNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "assetRegID=" + assetRegID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "detailNum=" + detailNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSortedFASchedules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSortedFASchedules
   Description: Gets and sorts the FASchedule/FATran records by FiscalYear/FiscalPeriod.
   OperationID: GetSortedFASchedules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSortedFASchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortedFASchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFASchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFASchedule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFASchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFASchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFASchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFATran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFATran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFATran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFATran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFATran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAScheduleListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAScheduleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FATranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FATranRow] = obj["value"]
      pass

class Erp_Tablesets_FAScheduleListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  company of asset transactions  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.DetailNum:int = obj["DetailNum"]
      """  Unique sequence number of the asset trransactions  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of last posted gl entry of this transaction.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of last posted gl entry of this transaction.  """  
      self.Depreciation:int = obj["Depreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.BookValue:int = obj["BookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostDate:str = obj["PostDate"]
      """  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  """  
      self.Posted:bool = obj["Posted"]
      """  flag to indicate the transaction is posted at least once.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  The class of the asset.  """  
      self.PostedDepreciation:int = obj["PostedDepreciation"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Closed:bool = obj["Closed"]
      """  The transaction is closed  when the fiscal period is closed for assets.  """  
      self.Modified:bool = obj["Modified"]
      """  for future use.  """  
      self.DocDepreciation:int = obj["DocDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedDepreciation:int = obj["DocPostedDepreciation"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1Depreciation:int = obj["Rpt1Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedDepreciation:int = obj["Rpt1PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2Depreciation:int = obj["Rpt2Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedDepreciation:int = obj["Rpt2PostedDepreciation"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3Depreciation:int = obj["Rpt3Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedDepreciation:int = obj["Rpt3PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.YearNum:int = obj["YearNum"]
      """  Year number not related to the fiscal year.  """  
      self.GrantDepreciation:int = obj["GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostedGrantDepn:int = obj["PostedGrantDepn"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DocGrantDepreciation:int = obj["DocGrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedGrantDepn:int = obj["DocPostedGrantDepn"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1GrantDepreciation:int = obj["Rpt1GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedGrantDepn:int = obj["Rpt1PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2GrantDepreciation:int = obj["Rpt2GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedGrantDepn:int = obj["Rpt2PostedGrantDepn"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3GrantDepreciation:int = obj["Rpt3GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedGrantDepn:int = obj["Rpt3PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.DepDetailNum:int = obj["DepDetailNum"]
      """  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  """  
      self.DepYear:int = obj["DepYear"]
      """  The depreciation year of last posted gl entry of this transaction.  """  
      self.DepYearSuffix:str = obj["DepYearSuffix"]
      """  Depreciation year suffix.  """  
      self.DepPeriod:int = obj["DepPeriod"]
      """  The depreciation period of last posted gl entry of this transaction.  """  
      self.PeriodHoliday:bool = obj["PeriodHoliday"]
      """  flag to indicate if the depreciation for this period is for holiday period and should not be included.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency Symbol  """  
      self.DispDetailNum:int = obj["DispDetailNum"]
      """  New sort order according to FiscalYear/FiscalPeriod  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAScheduleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  company of asset transactions  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.DetailNum:int = obj["DetailNum"]
      """  Unique sequence number of the asset trransactions  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of last posted gl entry of this transaction.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of last posted gl entry of this transaction.  """  
      self.Depreciation:int = obj["Depreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.BookValue:int = obj["BookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostDate:str = obj["PostDate"]
      """  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  """  
      self.Posted:bool = obj["Posted"]
      """  flag to indicate the transaction is posted at least once.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  The class of the asset.  """  
      self.PostedDepreciation:int = obj["PostedDepreciation"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Closed:bool = obj["Closed"]
      """  The transaction is closed  when the fiscal period is closed for assets.  """  
      self.Modified:bool = obj["Modified"]
      """  for future use.  """  
      self.DocDepreciation:int = obj["DocDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedDepreciation:int = obj["DocPostedDepreciation"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1Depreciation:int = obj["Rpt1Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedDepreciation:int = obj["Rpt1PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2Depreciation:int = obj["Rpt2Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedDepreciation:int = obj["Rpt2PostedDepreciation"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3Depreciation:int = obj["Rpt3Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedDepreciation:int = obj["Rpt3PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.YearNum:int = obj["YearNum"]
      """  Year number not related to the fiscal year.  """  
      self.GrantDepreciation:int = obj["GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostedGrantDepn:int = obj["PostedGrantDepn"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DocGrantDepreciation:int = obj["DocGrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedGrantDepn:int = obj["DocPostedGrantDepn"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1GrantDepreciation:int = obj["Rpt1GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedGrantDepn:int = obj["Rpt1PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2GrantDepreciation:int = obj["Rpt2GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedGrantDepn:int = obj["Rpt2PostedGrantDepn"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3GrantDepreciation:int = obj["Rpt3GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedGrantDepn:int = obj["Rpt3PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.DepDetailNum:int = obj["DepDetailNum"]
      """  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  """  
      self.DepYear:int = obj["DepYear"]
      """  The depreciation year of last posted gl entry of this transaction.  """  
      self.DepYearSuffix:str = obj["DepYearSuffix"]
      """  Depreciation year suffix.  """  
      self.DepPeriod:int = obj["DepPeriod"]
      """  The depreciation period of last posted gl entry of this transaction.  """  
      self.PeriodHoliday:bool = obj["PeriodHoliday"]
      """  flag to indicate if the depreciation for this period is for holiday period and should not be included.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency Symbol  """  
      self.DispDetailNum:int = obj["DispDetailNum"]
      """  New sort order according to FiscalYear/FiscalPeriod  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FATranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  company of asset transactions  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.DetailNum:int = obj["DetailNum"]
      """  Unique detail number of the asset depreciation transaction  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Unique sequence number of the asset depreciation transaction  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  Sequence of the Asset. Currently only 0 is supported.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of last posted gl entry of this transaction.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of last posted gl entry of this transaction.  """  
      self.Depreciation:int = obj["Depreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.BookValue:int = obj["BookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostDate:str = obj["PostDate"]
      """  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The gl journal of the last posting to the gl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The journal number of the last posting to the gl.  """  
      self.Posted:bool = obj["Posted"]
      """  flag to indicate the transaction is posted at least once.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  The class of the asset.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user who posted the transaction the last time.  """  
      self.PostValue:int = obj["PostValue"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the post value than the difference will be posted during the next posting process.  """  
      self.Closed:bool = obj["Closed"]
      """  The transaction is closed  when the fiscal period is closed for assets.  """  
      self.Modified:bool = obj["Modified"]
      """  for future use.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.DocDepreciation:int = obj["DocDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostValue:int = obj["DocPostValue"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1Depreciation:int = obj["Rpt1Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostValue:int = obj["Rpt1PostValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2Depreciation:int = obj["Rpt2Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostValue:int = obj["Rpt2PostValue"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3Depreciation:int = obj["Rpt3Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostValue:int = obj["Rpt3PostValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.YearNum:int = obj["YearNum"]
      """  Year number not related to the fiscal year.  """  
      self.GrantDepreciation:int = obj["GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostGrantValue:int = obj["PostGrantValue"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DocGrantDepreciation:int = obj["DocGrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostGrantValue:int = obj["DocPostGrantValue"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1GrantDepreciation:int = obj["Rpt1GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostGrantValue:int = obj["Rpt1PostGrantValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2GrantDepreciation:int = obj["Rpt2GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostGrantValue:int = obj["Rpt2PostGrantValue"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3GrantDepreciation:int = obj["Rpt3GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostGrantValue:int = obj["Rpt3PostGrantValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.DepDetailNum:int = obj["DepDetailNum"]
      """  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  """  
      self.DepYear:int = obj["DepYear"]
      """  The depreciation year of last posted gl entry of this transaction.  """  
      self.DepYearSuffix:str = obj["DepYearSuffix"]
      """  Depreciation year suffix.  """  
      self.DepPeriod:int = obj["DepPeriod"]
      """  The depreciation period of last posted gl entry of this transaction.  """  
      self.PeriodHoliday:bool = obj["PeriodHoliday"]
      """  flag to indicate if the depreciation for this period is for holiday period and should not be included.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranType:int = obj["TranType"]
      """  Source of depreciation transaction.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.SrcTranNum:int = obj["SrcTranNum"]
      """  SrcTranNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   assetNum
   assetRegID
   detailNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.assetRegID:str = obj["assetRegID"]
      self.detailNum:int = obj["detailNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FAScheduleListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  company of asset transactions  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.DetailNum:int = obj["DetailNum"]
      """  Unique sequence number of the asset trransactions  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of last posted gl entry of this transaction.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of last posted gl entry of this transaction.  """  
      self.Depreciation:int = obj["Depreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.BookValue:int = obj["BookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostDate:str = obj["PostDate"]
      """  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  """  
      self.Posted:bool = obj["Posted"]
      """  flag to indicate the transaction is posted at least once.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  The class of the asset.  """  
      self.PostedDepreciation:int = obj["PostedDepreciation"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Closed:bool = obj["Closed"]
      """  The transaction is closed  when the fiscal period is closed for assets.  """  
      self.Modified:bool = obj["Modified"]
      """  for future use.  """  
      self.DocDepreciation:int = obj["DocDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedDepreciation:int = obj["DocPostedDepreciation"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1Depreciation:int = obj["Rpt1Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedDepreciation:int = obj["Rpt1PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2Depreciation:int = obj["Rpt2Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedDepreciation:int = obj["Rpt2PostedDepreciation"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3Depreciation:int = obj["Rpt3Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedDepreciation:int = obj["Rpt3PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.YearNum:int = obj["YearNum"]
      """  Year number not related to the fiscal year.  """  
      self.GrantDepreciation:int = obj["GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostedGrantDepn:int = obj["PostedGrantDepn"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DocGrantDepreciation:int = obj["DocGrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedGrantDepn:int = obj["DocPostedGrantDepn"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1GrantDepreciation:int = obj["Rpt1GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedGrantDepn:int = obj["Rpt1PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2GrantDepreciation:int = obj["Rpt2GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedGrantDepn:int = obj["Rpt2PostedGrantDepn"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3GrantDepreciation:int = obj["Rpt3GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedGrantDepn:int = obj["Rpt3PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.DepDetailNum:int = obj["DepDetailNum"]
      """  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  """  
      self.DepYear:int = obj["DepYear"]
      """  The depreciation year of last posted gl entry of this transaction.  """  
      self.DepYearSuffix:str = obj["DepYearSuffix"]
      """  Depreciation year suffix.  """  
      self.DepPeriod:int = obj["DepPeriod"]
      """  The depreciation period of last posted gl entry of this transaction.  """  
      self.PeriodHoliday:bool = obj["PeriodHoliday"]
      """  flag to indicate if the depreciation for this period is for holiday period and should not be included.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency Symbol  """  
      self.DispDetailNum:int = obj["DispDetailNum"]
      """  New sort order according to FiscalYear/FiscalPeriod  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAScheduleListTableset:
   def __init__(self, obj):
      self.FAScheduleList:list[Erp_Tablesets_FAScheduleListRow] = obj["FAScheduleList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAScheduleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  company of asset transactions  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.DetailNum:int = obj["DetailNum"]
      """  Unique sequence number of the asset trransactions  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of last posted gl entry of this transaction.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of last posted gl entry of this transaction.  """  
      self.Depreciation:int = obj["Depreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.BookValue:int = obj["BookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostDate:str = obj["PostDate"]
      """  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  """  
      self.Posted:bool = obj["Posted"]
      """  flag to indicate the transaction is posted at least once.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  The class of the asset.  """  
      self.PostedDepreciation:int = obj["PostedDepreciation"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Closed:bool = obj["Closed"]
      """  The transaction is closed  when the fiscal period is closed for assets.  """  
      self.Modified:bool = obj["Modified"]
      """  for future use.  """  
      self.DocDepreciation:int = obj["DocDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedDepreciation:int = obj["DocPostedDepreciation"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1Depreciation:int = obj["Rpt1Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedDepreciation:int = obj["Rpt1PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2Depreciation:int = obj["Rpt2Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedDepreciation:int = obj["Rpt2PostedDepreciation"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3Depreciation:int = obj["Rpt3Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedDepreciation:int = obj["Rpt3PostedDepreciation"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.YearNum:int = obj["YearNum"]
      """  Year number not related to the fiscal year.  """  
      self.GrantDepreciation:int = obj["GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostedGrantDepn:int = obj["PostedGrantDepn"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DocGrantDepreciation:int = obj["DocGrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostedGrantDepn:int = obj["DocPostedGrantDepn"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1GrantDepreciation:int = obj["Rpt1GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostedGrantDepn:int = obj["Rpt1PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2GrantDepreciation:int = obj["Rpt2GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostedGrantDepn:int = obj["Rpt2PostedGrantDepn"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3GrantDepreciation:int = obj["Rpt3GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostedGrantDepn:int = obj["Rpt3PostedGrantDepn"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.DepDetailNum:int = obj["DepDetailNum"]
      """  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  """  
      self.DepYear:int = obj["DepYear"]
      """  The depreciation year of last posted gl entry of this transaction.  """  
      self.DepYearSuffix:str = obj["DepYearSuffix"]
      """  Depreciation year suffix.  """  
      self.DepPeriod:int = obj["DepPeriod"]
      """  The depreciation period of last posted gl entry of this transaction.  """  
      self.PeriodHoliday:bool = obj["PeriodHoliday"]
      """  flag to indicate if the depreciation for this period is for holiday period and should not be included.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency Symbol  """  
      self.DispDetailNum:int = obj["DispDetailNum"]
      """  New sort order according to FiscalYear/FiscalPeriod  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FATranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  company of asset transactions  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.DetailNum:int = obj["DetailNum"]
      """  Unique detail number of the asset depreciation transaction  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Unique sequence number of the asset depreciation transaction  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  Sequence of the Asset. Currently only 0 is supported.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of last posted gl entry of this transaction.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of last posted gl entry of this transaction.  """  
      self.Depreciation:int = obj["Depreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.BookValue:int = obj["BookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostDate:str = obj["PostDate"]
      """  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The gl journal of the last posting to the gl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The journal number of the last posting to the gl.  """  
      self.Posted:bool = obj["Posted"]
      """  flag to indicate the transaction is posted at least once.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  The class of the asset.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The user who posted the transaction the last time.  """  
      self.PostValue:int = obj["PostValue"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the post value than the difference will be posted during the next posting process.  """  
      self.Closed:bool = obj["Closed"]
      """  The transaction is closed  when the fiscal period is closed for assets.  """  
      self.Modified:bool = obj["Modified"]
      """  for future use.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.DocDepreciation:int = obj["DocDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostValue:int = obj["DocPostValue"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1Depreciation:int = obj["Rpt1Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostValue:int = obj["Rpt1PostValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2Depreciation:int = obj["Rpt2Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostValue:int = obj["Rpt2PostValue"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3Depreciation:int = obj["Rpt3Depreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostValue:int = obj["Rpt3PostValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.YearNum:int = obj["YearNum"]
      """  Year number not related to the fiscal year.  """  
      self.GrantDepreciation:int = obj["GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction.  """  
      self.PostGrantValue:int = obj["PostGrantValue"]
      """  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DocGrantDepreciation:int = obj["DocGrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in the document currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in the document currency.  """  
      self.DocPostGrantValue:int = obj["DocPostGrantValue"]
      """  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt1GrantDepreciation:int = obj["Rpt1GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt1PostGrantValue:int = obj["Rpt1PostGrantValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt2GrantDepreciation:int = obj["Rpt2GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  The bookvalue of the asset after posting this transaction in reporting currency.  """  
      self.Rpt2PostGrantValue:int = obj["Rpt2PostGrantValue"]
      """  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.Rpt3GrantDepreciation:int = obj["Rpt3GrantDepreciation"]
      """  The depreciation amount of the asset for this transaction in reporting currency.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  The bookvalue of the asset after posting this treansaction in reporting currency.  """  
      self.Rpt3PostGrantValue:int = obj["Rpt3PostGrantValue"]
      """  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.DepDetailNum:int = obj["DepDetailNum"]
      """  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  """  
      self.DepYear:int = obj["DepYear"]
      """  The depreciation year of last posted gl entry of this transaction.  """  
      self.DepYearSuffix:str = obj["DepYearSuffix"]
      """  Depreciation year suffix.  """  
      self.DepPeriod:int = obj["DepPeriod"]
      """  The depreciation period of last posted gl entry of this transaction.  """  
      self.PeriodHoliday:bool = obj["PeriodHoliday"]
      """  flag to indicate if the depreciation for this period is for holiday period and should not be included.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranType:int = obj["TranType"]
      """  Source of depreciation transaction.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.SrcTranNum:int = obj["SrcTranNum"]
      """  SrcTranNum  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FATranSearchTableset:
   def __init__(self, obj):
      self.FASchedule:list[Erp_Tablesets_FAScheduleRow] = obj["FASchedule"]
      self.FATran:list[Erp_Tablesets_FATranRow] = obj["FATran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFATranSearchTableset:
   def __init__(self, obj):
      self.FASchedule:list[Erp_Tablesets_FAScheduleRow] = obj["FASchedule"]
      self.FATran:list[Erp_Tablesets_FATranRow] = obj["FATran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   assetNum
   assetRegID
   detailNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.assetRegID:str = obj["assetRegID"]
      self.detailNum:int = obj["detailNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FATranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FATranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FATranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAScheduleListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFASchedule_input:
   """ Required : 
   ds
   assetNum
   assetRegID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.assetRegID:str = obj["assetRegID"]
      pass

class GetNewFASchedule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFATran_input:
   """ Required : 
   ds
   assetNum
   assetRegID
   detailNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.assetRegID:str = obj["assetRegID"]
      self.detailNum:int = obj["detailNum"]
      pass

class GetNewFATran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFASchedule
   whereClauseFATran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFASchedule:str = obj["whereClauseFASchedule"]
      self.whereClauseFATran:str = obj["whereClauseFATran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FATranSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSortedFASchedules_input:
   """ Required : 
   ipAssetNum
   ipAssetRegID
   ds
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  Input AssetNum  """  
      self.ipAssetRegID:str = obj["ipAssetRegID"]
      """  Input Asset Register ID  """  
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      pass

class GetSortedFASchedules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFATranSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFATranSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FATranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

