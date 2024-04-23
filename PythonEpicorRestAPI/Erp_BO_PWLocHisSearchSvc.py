import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PWLocHisSearchSvc
# Description: Part Locations Wip Search Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PWLocHisSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PWLocHisSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PWLocHisSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PWLocHisRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches",headers=creds) as resp:
           return await resp.json()

async def post_PWLocHisSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PWLocHisSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PWLocHisSearches_Company_Plant_JobNum_PartNum_DateTimeControl_AssemblySeq_OprSeq_MtlSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_PCID_AttributeSetID(Company, Plant, JobNum, PartNum, DateTimeControl, AssemblySeq, OprSeq, MtlSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, PCID, AttributeSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PWLocHisSearch item
   Description: Calls GetByID to retrieve the PWLocHisSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PWLocHisSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DateTimeControl: Desc: DateTimeControl   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches(" + Company + "," + Plant + "," + JobNum + "," + PartNum + "," + DateTimeControl + "," + AssemblySeq + "," + OprSeq + "," + MtlSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + PCID + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PWLocHisSearches_Company_Plant_JobNum_PartNum_DateTimeControl_AssemblySeq_OprSeq_MtlSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_PCID_AttributeSetID(Company, Plant, JobNum, PartNum, DateTimeControl, AssemblySeq, OprSeq, MtlSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, PCID, AttributeSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PWLocHisSearch for the service
   Description: Calls UpdateExt to update PWLocHisSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PWLocHisSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DateTimeControl: Desc: DateTimeControl   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches(" + Company + "," + Plant + "," + JobNum + "," + PartNum + "," + DateTimeControl + "," + AssemblySeq + "," + OprSeq + "," + MtlSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + PCID + "," + AttributeSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PWLocHisSearches_Company_Plant_JobNum_PartNum_DateTimeControl_AssemblySeq_OprSeq_MtlSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_PCID_AttributeSetID(Company, Plant, JobNum, PartNum, DateTimeControl, AssemblySeq, OprSeq, MtlSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, PCID, AttributeSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PWLocHisSearch item
   Description: Call UpdateExt to delete PWLocHisSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PWLocHisSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DateTimeControl: Desc: DateTimeControl   Required: True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches(" + Company + "," + Plant + "," + JobNum + "," + PartNum + "," + DateTimeControl + "," + AssemblySeq + "," + OprSeq + "," + MtlSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + PCID + "," + AttributeSetID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PWLocHisListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePWLocHis, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClausePWLocHis=" + whereClausePWLocHis
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, jobNum, partNum, dateTimeControl, assemblySeq, oprSeq, mtlSeq, wareHouseCode, binNum, lotNum, dimCode, trackType, pcID, attributeSetID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "jobNum=" + jobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "dateTimeControl=" + dateTimeControl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "assemblySeq=" + assemblySeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "oprSeq=" + oprSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mtlSeq=" + mtlSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "wareHouseCode=" + wareHouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "binNum=" + binNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "lotNum=" + lotNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "dimCode=" + dimCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "trackType=" + trackType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcID=" + pcID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attributeSetID=" + attributeSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetJobInspectionsData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobInspectionsData
   Description: Retrieves Part Locations Inspections related to a Job
   OperationID: GetJobInspectionsData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobInspectionsData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobInspectionsData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartInspectionsData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartInspectionsData
   Description: Retrieves Part Locations Inspections related to a Part
   OperationID: GetPartInspectionsData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInspectionsData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInspectionsData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPWLocHis(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPWLocHis
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPWLocHis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPWLocHis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPWLocHis_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PWLocHisListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PWLocHisRow] = obj["value"]
      pass

class Erp_Tablesets_PWLocHisListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID that created the record.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date that record was created.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  System time record was created.(secounds from midnight).  """  
      self.DateTimeControl:int = obj["DateTimeControl"]
      """   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TrackTypeDescription:str = obj["TrackTypeDescription"]
      """  Description for the TrackType column  """  
      self.DispCreatedTime:str = obj["DispCreatedTime"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PWLocHisRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID that created the record.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date that record was created.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  System time record was created.(secounds from midnight).  """  
      self.DateTimeControl:int = obj["DateTimeControl"]
      """   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TrackTypeDescription:str = obj["TrackTypeDescription"]
      """  Description for the TrackType column  """  
      self.DispCreatedTime:str = obj["DispCreatedTime"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpMasterOpDesc:str = obj["OpMasterOpDesc"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   jobNum
   partNum
   dateTimeControl
   assemblySeq
   oprSeq
   mtlSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   pcID
   attributeSetID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      self.dateTimeControl:int = obj["dateTimeControl"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PWInspectDSTableset:
   def __init__(self, obj):
      self.PWInspect:list[Erp_Tablesets_PWInspectRow] = obj["PWInspect"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PWInspectRow:
   def __init__(self, obj):
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job  """  
      self.JobSeq:int = obj["JobSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies the part that comes from the RcvDtl or NonConf table record.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exis  """  
      self.Quantity:int = obj["Quantity"]
      """  Transaction Quantity  """  
      self.RecordType:str = obj["RecordType"]
      """  Description of the Inspection record which depends on the table that the information comes from. If the record comes from the RcvDtl table this type is set to "Receipt", if it comes from the NonConf this type is set to "Assemblies", "Inventory", "Materials" depending on the NonConf.TrnTyp field being "D", "I" or "M" respectively.  """  
      self.Revision:str = obj["Revision"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.SeqType:str = obj["SeqType"]
      """  Denotes the JobSeqType and is set to "MTL" if the JobSeqType or the TrnTyp of the RcvDtl or NonConf record respectively equals "M", or it is set to "SUB" when it equals "S".  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for the warehouse that comes from the RcvDtl or NonConf table.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.Name:str = obj["Name"]
      """  Vendor's or Customer's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  TranID of related NonConf record.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Warehouse Description.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of Pieces  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PWLocHisListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID that created the record.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date that record was created.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  System time record was created.(secounds from midnight).  """  
      self.DateTimeControl:int = obj["DateTimeControl"]
      """   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TrackTypeDescription:str = obj["TrackTypeDescription"]
      """  Description for the TrackType column  """  
      self.DispCreatedTime:str = obj["DispCreatedTime"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PWLocHisListTableset:
   def __init__(self, obj):
      self.PWLocHisList:list[Erp_Tablesets_PWLocHisListRow] = obj["PWLocHisList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PWLocHisRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID that created the record.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date that record was created.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  System time record was created.(secounds from midnight).  """  
      self.DateTimeControl:int = obj["DateTimeControl"]
      """   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TrackTypeDescription:str = obj["TrackTypeDescription"]
      """  Description for the TrackType column  """  
      self.DispCreatedTime:str = obj["DispCreatedTime"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpMasterOpDesc:str = obj["OpMasterOpDesc"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PWLocHisSearchTableset:
   def __init__(self, obj):
      self.PWLocHis:list[Erp_Tablesets_PWLocHisRow] = obj["PWLocHis"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPWLocHisSearchTableset:
   def __init__(self, obj):
      self.PWLocHis:list[Erp_Tablesets_PWLocHisRow] = obj["PWLocHis"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   jobNum
   partNum
   dateTimeControl
   assemblySeq
   oprSeq
   mtlSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   pcID
   attributeSetID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      self.dateTimeControl:int = obj["dateTimeControl"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.pcID:str = obj["pcID"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["returnObj"]
      pass

class GetJobInspectionsData_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      pass

class GetJobInspectionsData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PWInspectDSTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PWLocHisListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPWLocHis_input:
   """ Required : 
   ds
   plant
   jobNum
   partNum
   dateTimeControl
   assemblySeq
   oprSeq
   mtlSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   pcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.jobNum:str = obj["jobNum"]
      self.partNum:str = obj["partNum"]
      self.dateTimeControl:int = obj["dateTimeControl"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.pcID:str = obj["pcID"]
      pass

class GetNewPWLocHis_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartInspectionsData_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Job Number  """  
      pass

class GetPartInspectionsData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PWInspectDSTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePWLocHis
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePWLocHis:str = obj["whereClausePWLocHis"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPWLocHisSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPWLocHisSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PWLocHisSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

