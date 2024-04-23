import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APInvoiceLoadSvc
# Description: A/P Open Invoice Load Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APInvoiceLoads(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APInvoiceLoads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvoiceLoads
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceLoadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads",headers=creds) as resp:
           return await resp.json()

async def post_APInvoiceLoads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvoiceLoads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvoiceLoadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvoiceLoadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APInvoiceLoads_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APInvoiceLoad item
   Description: Calls GetByID to retrieve the APInvoiceLoad item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvoiceLoad
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvoiceLoadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APInvoiceLoads_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APInvoiceLoad for the service
   Description: Calls UpdateExt to update APInvoiceLoad. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvoiceLoad
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvoiceLoadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APInvoiceLoads_Company_VendorNum_InvoiceNum(Company, VendorNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APInvoiceLoad item
   Description: Call UpdateExt to delete APInvoiceLoad item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvoiceLoad
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_APInvoiceLoads_Company_VendorNum_InvoiceNum_EntityGLCs(Company, VendorNum, InvoiceNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_APInvoiceLoads_Company_VendorNum_InvoiceNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, VendorNum, InvoiceNum, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/APInvoiceLoads(" + Company + "," + VendorNum + "," + InvoiceNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvoiceLoadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPInvoiceLoad, whereClauseEntityGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPInvoiceLoad=" + whereClauseAPInvoiceLoad
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, invoiceNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeApplyDate
   Description: This method updates the A/P Apply Date
   OperationID: ChangeApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInvoiceBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInvoiceBalance
   Description: This method updates the A/P Invoice Amounts when the invoice balance changes or
the exchange rate changes.  Use the external fields APInvoiceLoad.DispInvoiceBal
and APInvoiceLoad.DocDispInvoiceBal to accept the user entered amount.  An input
parameter is expected to indicate if this method is called after changing the
Exchange Rate or the Base Invoice Balance or the Doc Invoice Balance.  When changing
the actual InvoiceBal and DocInvoiceBal fields instead of the Disp counterparts,
set the Change Type to be: 'B1' and 'D1' for base and doc fields.
   OperationID: ChangeInvoiceBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInvoiceDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInvoiceDate
   Description: This method updates the A/P Invoice Dates and Exchange Rates when the Invoice
Date changes and checks if the date is greater than the client today date.
This method will additionally return a message to present to the user if necessary.
   OperationID: ChangeInvoiceDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingInvoiceOrApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingInvoiceOrApplyDate
   Description: This method verifies the invoice date and/or apply date
   OperationID: OnChangingInvoiceOrApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingInvoiceOrApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingInvoiceOrApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTerms(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTerms
   Description: This method updates the A/P Invoice Due Date when the Terms Code changes.
   OperationID: ChangeTerms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTerms_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTerms_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorID
   Description: This method defaults the A/P Invoice Load details based on the proposed Vendor ID.
   OperationID: ChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Change1099Code(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Change1099Code
   OperationID: Change1099Code
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Change1099Code_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Change1099Code_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFormType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFormType
   OperationID: ChangeFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCurrencyCodeOrRateGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCurrencyCodeOrRateGroup
   Description: This method is executed when changing the currency code or rate type, then calls the method GetExchangeRate to return the correct exchange rate.
   OperationID: OnChangeCurrencyCodeOrRateGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCurrencyCodeOrRateGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCurrencyCodeOrRateGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPInvoiceLoad1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPInvoiceLoad1
   Description: This method is to be used in place of GetNewAPInvoiceLoad.
   OperationID: GetNewAPInvoiceLoad1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvoiceLoad1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvoiceLoad1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxTypesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxTypesList
   Description: Get where clause to select tax types, related to specified Tax Liability
   OperationID: GetTaxTypesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxTypesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxTypesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTotalBalance(epicorHeaders = None):
   """  
   Summary: Invoke method GetTotalBalance
   Description: This method returns the total unposted invoice load balance and the base
currency symbol.
   OperationID: GetTotalBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTotalBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTax
   Description: Called when the Tax Type or Tax Rate field changes.
   OperationID: OnChangingTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostOpenInvLoad(epicorHeaders = None):
   """  
   Summary: Invoke method PostOpenInvLoad
   Description: This method performs the actual posting of open invoice loads. It is assumed
that the user already okayed to continue with the posting.
   OperationID: PostOpenInvLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostOpenInvLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendBankID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendBankID
   Description: Call this method when the user enters the ttApInv.BankID
   OperationID: OnChangeVendBankID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendBankID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendBankID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateVendorID
   Description: Validates the vendor ID
   OperationID: ValidateVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePLInvoiceReference(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePLInvoiceReference
   Description: CSF Poland. Validate unique of PLInvoiceReference for selected supplier
   OperationID: ValidatePLInvoiceReference
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePLInvoiceReference_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePLInvoiceReference_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPInvoiceLoad(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPInvoiceLoad
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvoiceLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvoiceLoad_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvoiceLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvoiceLoadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvoiceLoadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvoiceLoadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvoiceLoadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Erp_Tablesets_APInvoiceLoadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall invoice.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.UpdateTax:bool = obj["UpdateTax"]
      """  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identification of the Invoice.  """  
      self.FixedAmt:bool = obj["FixedAmt"]
      """  Allows user to control discount amount manually or automatically  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  """  
      self.CPayLegalNumber:str = obj["CPayLegalNumber"]
      """  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlType:str = obj["GLControlType"]
      """  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt1CPayInvoiceBal:int = obj["Rpt1CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt2CPayInvoiceBal:int = obj["Rpt2CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt3CPayInvoiceBal:int = obj["Rpt3CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.AllowOverrideLI:bool = obj["AllowOverrideLI"]
      """  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  """  
      self.MatchedFromLI:bool = obj["MatchedFromLI"]
      """  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.GUIImportTaxBasis:int = obj["GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis  """  
      self.DocGUIImportTaxBasis:int = obj["DocGUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in document currrency  """  
      self.Rpt1GUIImportTaxBasis:int = obj["Rpt1GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt1 currency  """  
      self.Rpt2GUIImportTaxBasis:int = obj["Rpt2GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt2 currency  """  
      self.Rpt3GUIImportTaxBasis:int = obj["Rpt3GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked flag  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  The claim reference from the expense group that generated the invoice.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee from the group of expenses that created the invoice.  """  
      self.InBankFile:bool = obj["InBankFile"]
      """  Indicates that Invoice has been selected for payment in a bankfile  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Credit Note Confirmation Date  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.SelfLegalNumber:str = obj["SelfLegalNumber"]
      """  Legal Number for the self assessment.  """  
      self.SelfTranDocTypeID:str = obj["SelfTranDocTypeID"]
      """  Transaction Document Type for the self assessment.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.SupAgentName:str = obj["SupAgentName"]
      """  Supplier Agent Name  """  
      self.SupAgentTaxRegNo:str = obj["SupAgentTaxRegNo"]
      """  Supplier Agent Tax Region Number  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.NonDeductVATAmt:int = obj["NonDeductVATAmt"]
      """  Non Deductable VAT Amount  """  
      self.NonDeductVATDocAmt:int = obj["NonDeductVATDocAmt"]
      """  Non Deductable VAT Doc Amount  """  
      self.NonDeductVATRpt1Amt:int = obj["NonDeductVATRpt1Amt"]
      """  Non Deductable VAT Rpt1 Amount  """  
      self.NonDeductVATRpt2Amt:int = obj["NonDeductVATRpt2Amt"]
      """  Non Deductable VAT Rpt2 Amount  """  
      self.NonDeductVATRpt3Amt:int = obj["NonDeductVATRpt3Amt"]
      """  Non Deductable VAT Rpt3 Amount  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:str = obj["ImportedFrom"]
      """  Country of Import  """  
      self.ImportedDate:str = obj["ImportedDate"]
      """  Date of import.  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates that this is Advanced Tax invoice received from
supplier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.DispInvoiceBal:int = obj["DispInvoiceBal"]
      """  Display field for Invoice Balance  """  
      self.DocDispInvoiceBal:int = obj["DocDispInvoiceBal"]
      """  Display field for DocInvoiceBal  """  
      self.UseLegalNumber:bool = obj["UseLegalNumber"]
      """  Flag to indicate if the Legal Number should be enabled.  """  
      self.Rpt1DispInvoiceBal:int = obj["Rpt1DispInvoiceBal"]
      self.Rpt2DispInvoiceBal:int = obj["Rpt2DispInvoiceBal"]
      self.Rpt3DispInvoiceBal:int = obj["Rpt3DispInvoiceBal"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      """  GL Control description.  """  
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      """  GL Control Type description  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.TermsDescription:str = obj["TermsDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceLoadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall invoice.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.UpdateTax:bool = obj["UpdateTax"]
      """  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identification of the Invoice.  """  
      self.FixedAmt:bool = obj["FixedAmt"]
      """  Allows user to control discount amount manually or automatically  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  """  
      self.CPayLegalNumber:str = obj["CPayLegalNumber"]
      """  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlType:str = obj["GLControlType"]
      """  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt1CPayInvoiceBal:int = obj["Rpt1CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt2CPayInvoiceBal:int = obj["Rpt2CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt3CPayInvoiceBal:int = obj["Rpt3CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.AllowOverrideLI:bool = obj["AllowOverrideLI"]
      """  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  """  
      self.MatchedFromLI:bool = obj["MatchedFromLI"]
      """  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.GUIImportTaxBasis:int = obj["GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis  """  
      self.DocGUIImportTaxBasis:int = obj["DocGUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in document currrency  """  
      self.Rpt1GUIImportTaxBasis:int = obj["Rpt1GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt1 currency  """  
      self.Rpt2GUIImportTaxBasis:int = obj["Rpt2GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt2 currency  """  
      self.Rpt3GUIImportTaxBasis:int = obj["Rpt3GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked flag  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  The claim reference from the expense group that generated the invoice.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee from the group of expenses that created the invoice.  """  
      self.InBankFile:bool = obj["InBankFile"]
      """  Indicates that Invoice has been selected for payment in a bankfile  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Credit Note Confirmation Date  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.SelfLegalNumber:str = obj["SelfLegalNumber"]
      """  Legal Number for the self assessment.  """  
      self.SelfTranDocTypeID:str = obj["SelfTranDocTypeID"]
      """  Transaction Document Type for the self assessment.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.SupAgentName:str = obj["SupAgentName"]
      """  Supplier Agent Name  """  
      self.SupAgentTaxRegNo:str = obj["SupAgentTaxRegNo"]
      """  Supplier Agent Tax Region Number  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.NonDeductVATAmt:int = obj["NonDeductVATAmt"]
      """  Non Deductable VAT Amount  """  
      self.NonDeductVATDocAmt:int = obj["NonDeductVATDocAmt"]
      """  Non Deductable VAT Doc Amount  """  
      self.NonDeductVATRpt1Amt:int = obj["NonDeductVATRpt1Amt"]
      """  Non Deductable VAT Rpt1 Amount  """  
      self.NonDeductVATRpt2Amt:int = obj["NonDeductVATRpt2Amt"]
      """  Non Deductable VAT Rpt2 Amount  """  
      self.NonDeductVATRpt3Amt:int = obj["NonDeductVATRpt3Amt"]
      """  Non Deductable VAT Rpt3 Amount  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:str = obj["ImportedFrom"]
      """  Country of Import  """  
      self.ImportedDate:str = obj["ImportedDate"]
      """  Date of import.  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates that this is Advanced Tax invoice received from
supplier  """  
      self.InPrice:bool = obj["InPrice"]
      """   Indicates that the tax is included in the unit price
for this AP Invoice  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Assigned as "I" when Recurring Invoice has Inactive status.  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsMaxValue:bool = obj["IsMaxValue"]
      """  IsMaxValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.DMReason:str = obj["DMReason"]
      """  DMReason  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.AGDocPageNum:str = obj["AGDocPageNum"]
      """  AGDocPageNum  """  
      self.AGCAICAEMark:str = obj["AGCAICAEMark"]
      """  AGCAICAEMark  """  
      self.AGCAICAENum:str = obj["AGCAICAENum"]
      """  AGCAICAENum  """  
      self.AGCAICAEExpirationDate:str = obj["AGCAICAEExpirationDate"]
      """  AGCAICAEExpirationDate  """  
      self.AGAvTaxCreditFlag:bool = obj["AGAvTaxCreditFlag"]
      """  AGAvTaxCreditFlag  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGCustomsClearanceNum:str = obj["AGCustomsClearanceNum"]
      """  AGCustomsClearanceNum  """  
      self.AGCustomsCode:str = obj["AGCustomsCode"]
      """  AGCustomsCode  """  
      self.AGDestinationCode:str = obj["AGDestinationCode"]
      """  AGDestinationCode  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Header Number  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.APChkGrpID:str = obj["APChkGrpID"]
      """  AP Checking Group ID  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.PEComputationalCost:str = obj["PEComputationalCost"]
      """  Indicates a computational cost for the invoice  """  
      self.ReferencedByBOE:str = obj["ReferencedByBOE"]
      """  Referenced By BOE  """  
      self.PEDUARefNum:str = obj["PEDUARefNum"]
      """  DUA Reference Number used on Peru Localiation  """  
      self.CustomsNumber:str = obj["CustomsNumber"]
      """  CustomsNumber  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  ReceivedDate  """  
      self.CustOverride:int = obj["CustOverride"]
      """  CustOverride  """  
      self.PrePaymentNum:str = obj["PrePaymentNum"]
      """  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  """  
      self.PrePaymentAmt:int = obj["PrePaymentAmt"]
      """  Pre-Payment amount in Base Currency.  """  
      self.DocPrePaymentAmt:int = obj["DocPrePaymentAmt"]
      """  Pre-Payment amount in Document Currency.  """  
      self.Rpt1PrePaymentAmt:int = obj["Rpt1PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt2PrePaymentAmt:int = obj["Rpt2PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt3PrePaymentAmt:int = obj["Rpt3PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  CSF Peru - AP Payment Number  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  SCF Peru - Detractions Tax Amount  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  Peru Detraction Tax Currency Code  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.DocPESUNATDepAmt:int = obj["DocPESUNATDepAmt"]
      """  Peru Document SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PESUNATNum:str = obj["PESUNATNum"]
      """  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  Document Tax Amount used in Peru detractions  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.PrePayHeadNum:int = obj["PrePayHeadNum"]
      """  PrePayHeadNum  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  Malaysia Import Declaration Number  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.GRNIClearing:bool = obj["GRNIClearing"]
      """  Flag that indicates if the invoice is a GRNI document.  """  
      self.PEFiscalCreditOperStatus:int = obj["PEFiscalCreditOperStatus"]
      """  CSF Peru - Fiscal Credit Operation Status  """  
      self.PEInternatTaxAgr:str = obj["PEInternatTaxAgr"]
      """  CSF Peru - International Tax agreement  """  
      self.PERentType:str = obj["PERentType"]
      """  CSF Peru - Rent type  """  
      self.PEPurchaseType:str = obj["PEPurchaseType"]
      """  CSF Peru - Purchase  type  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  TH Reference Invoice Num  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  TH Reference Vendor Num  """  
      self.JPSummarizationDate:str = obj["JPSummarizationDate"]
      """  Day when a company sums up accounts payable for supplier  """  
      self.JPBillingDate:str = obj["JPBillingDate"]
      """  Date of a Payment Statement  """  
      self.JPBillingNumber:str = obj["JPBillingNumber"]
      """  Legal Number of Payment Statement  """  
      self.SelfInvoice:bool = obj["SelfInvoice"]
      """  SelfInvoice  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.INPortCode:str = obj["INPortCode"]
      """  INPortCode  """  
      self.RefCancelledby:str = obj["RefCancelledby"]
      """  Indicates which invoice number has cancelled this invoice.  """  
      self.CancellationInv:bool = obj["CancellationInv"]
      """  Indicates if this invoice is a cancellation invoice.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  Source Plant used for multi site GL  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.CHQRIBAN:str = obj["CHQRIBAN"]
      """  CHQRIBAN  """  
      self.CHQRReference:str = obj["CHQRReference"]
      """  CHQRReference  """  
      self.EDIInvoice:bool = obj["EDIInvoice"]
      """  Set to True for any invoice that is created via EDI  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.Code1099Description:str = obj["Code1099Description"]
      """  1099 Code Description, defaults from Supplier  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code, defaults from Supplier  """  
      self.DispInvoiceBal:int = obj["DispInvoiceBal"]
      """  Display field for Invoice Balance  """  
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      """  Form Type Description  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates whether created invoice should be paid.  """  
      self.PLVendorAutoInvoiceNum:bool = obj["PLVendorAutoInvoiceNum"]
      """  CSF Poland. Vendor uses Invoice reference number  """  
      self.Print1099:bool = obj["Print1099"]
      self.Rpt1DispInvoiceBal:int = obj["Rpt1DispInvoiceBal"]
      self.Rpt2DispInvoiceBal:int = obj["Rpt2DispInvoiceBal"]
      self.Rpt3DispInvoiceBal:int = obj["Rpt3DispInvoiceBal"]
      self.TaxableAmt1:int = obj["TaxableAmt1"]
      """  Taxable Value 1  """  
      self.TaxableAmt2:int = obj["TaxableAmt2"]
      """  Taxable Value 2  """  
      self.TaxableAmt3:int = obj["TaxableAmt3"]
      """  Taxable Value 3  """  
      self.TaxableAmt4:int = obj["TaxableAmt4"]
      """  Taxable Value 4  """  
      self.TaxAmt1:int = obj["TaxAmt1"]
      """  Tax Value 1  """  
      self.TaxAmt2:int = obj["TaxAmt2"]
      """  Tax Value 2  """  
      self.TaxAmt3:int = obj["TaxAmt3"]
      """  Tax Value 3  """  
      self.TaxAmt4:int = obj["TaxAmt4"]
      """  Tax Value 4  """  
      self.TaxCode1:str = obj["TaxCode1"]
      """  Tax Type 1  """  
      self.TaxCode1Description:str = obj["TaxCode1Description"]
      self.TaxCode2:str = obj["TaxCode2"]
      """  Tax Type 2  """  
      self.TaxCode2Description:str = obj["TaxCode2Description"]
      self.TaxCode3:str = obj["TaxCode3"]
      """  Tax Type 3  """  
      self.TaxCode3Description:str = obj["TaxCode3Description"]
      self.TaxCode4:str = obj["TaxCode4"]
      """  Tax Type 4  """  
      self.TaxCode4Description:str = obj["TaxCode4Description"]
      self.TaxRate1:str = obj["TaxRate1"]
      """  Tax Rate 1  """  
      self.TaxRate1Description:str = obj["TaxRate1Description"]
      self.TaxRate2:str = obj["TaxRate2"]
      """  Tax Rate 2  """  
      self.TaxRate2Description:str = obj["TaxRate2Description"]
      self.TaxRate3:str = obj["TaxRate3"]
      """  Tax Rate 3  """  
      self.TaxRate3Description:str = obj["TaxRate3Description"]
      self.TaxRate4:str = obj["TaxRate4"]
      """  Tax Rate 4  """  
      self.TaxRate4Description:str = obj["TaxRate4Description"]
      self.UseLegalNumber:bool = obj["UseLegalNumber"]
      """  Flag to indicate if the Legal Number should be enabled.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.BankName:str = obj["BankName"]
      self.DocDispInvoiceBal:int = obj["DocDispInvoiceBal"]
      """  Display field for DocInvoiceBal  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Site is a legal entity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.SourcePlantName:str = obj["SourcePlantName"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.VendorName:str = obj["VendorName"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorState:str = obj["VendorState"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.XbSystIsDiscountforDebitM:bool = obj["XbSystIsDiscountforDebitM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Change1099Code_input:
   """ Required : 
   formTypeID
   proposedCode1099ID
   ds
   """  
   def __init__(self, obj):
      self.formTypeID:str = obj["formTypeID"]
      self.proposedCode1099ID:str = obj["proposedCode1099ID"]
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class Change1099Code_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeApplyDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class ChangeApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFormType_input:
   """ Required : 
   formType
   ds
   """  
   def __init__(self, obj):
      self.formType:str = obj["formType"]
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class ChangeFormType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeInvoiceBalance_input:
   """ Required : 
   ds
   ipChangeType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      self.ipChangeType:str = obj["ipChangeType"]
      """  Valid values: 'E' = Exchange Rate; 'B' = DispInvoiceBal; 'D' = DocDispInvoiceBal
            'B1' = InvoiceBal; 'D1' = DocInvoiceBal  """  
      pass

class ChangeInvoiceBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeInvoiceDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class ChangeInvoiceDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTerms_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class ChangeTerms_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorID_input:
   """ Required : 
   ds
   ipProposedVendorID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      self.ipProposedVendorID:str = obj["ipProposedVendorID"]
      """  The proposed Vendor ID  """  
      pass

class ChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APInvoiceLoadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall invoice.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.UpdateTax:bool = obj["UpdateTax"]
      """  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identification of the Invoice.  """  
      self.FixedAmt:bool = obj["FixedAmt"]
      """  Allows user to control discount amount manually or automatically  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  """  
      self.CPayLegalNumber:str = obj["CPayLegalNumber"]
      """  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlType:str = obj["GLControlType"]
      """  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt1CPayInvoiceBal:int = obj["Rpt1CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt2CPayInvoiceBal:int = obj["Rpt2CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt3CPayInvoiceBal:int = obj["Rpt3CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.AllowOverrideLI:bool = obj["AllowOverrideLI"]
      """  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  """  
      self.MatchedFromLI:bool = obj["MatchedFromLI"]
      """  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.GUIImportTaxBasis:int = obj["GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis  """  
      self.DocGUIImportTaxBasis:int = obj["DocGUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in document currrency  """  
      self.Rpt1GUIImportTaxBasis:int = obj["Rpt1GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt1 currency  """  
      self.Rpt2GUIImportTaxBasis:int = obj["Rpt2GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt2 currency  """  
      self.Rpt3GUIImportTaxBasis:int = obj["Rpt3GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked flag  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  The claim reference from the expense group that generated the invoice.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee from the group of expenses that created the invoice.  """  
      self.InBankFile:bool = obj["InBankFile"]
      """  Indicates that Invoice has been selected for payment in a bankfile  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Credit Note Confirmation Date  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.SelfLegalNumber:str = obj["SelfLegalNumber"]
      """  Legal Number for the self assessment.  """  
      self.SelfTranDocTypeID:str = obj["SelfTranDocTypeID"]
      """  Transaction Document Type for the self assessment.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.SupAgentName:str = obj["SupAgentName"]
      """  Supplier Agent Name  """  
      self.SupAgentTaxRegNo:str = obj["SupAgentTaxRegNo"]
      """  Supplier Agent Tax Region Number  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.NonDeductVATAmt:int = obj["NonDeductVATAmt"]
      """  Non Deductable VAT Amount  """  
      self.NonDeductVATDocAmt:int = obj["NonDeductVATDocAmt"]
      """  Non Deductable VAT Doc Amount  """  
      self.NonDeductVATRpt1Amt:int = obj["NonDeductVATRpt1Amt"]
      """  Non Deductable VAT Rpt1 Amount  """  
      self.NonDeductVATRpt2Amt:int = obj["NonDeductVATRpt2Amt"]
      """  Non Deductable VAT Rpt2 Amount  """  
      self.NonDeductVATRpt3Amt:int = obj["NonDeductVATRpt3Amt"]
      """  Non Deductable VAT Rpt3 Amount  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:str = obj["ImportedFrom"]
      """  Country of Import  """  
      self.ImportedDate:str = obj["ImportedDate"]
      """  Date of import.  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates that this is Advanced Tax invoice received from
supplier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.DispInvoiceBal:int = obj["DispInvoiceBal"]
      """  Display field for Invoice Balance  """  
      self.DocDispInvoiceBal:int = obj["DocDispInvoiceBal"]
      """  Display field for DocInvoiceBal  """  
      self.UseLegalNumber:bool = obj["UseLegalNumber"]
      """  Flag to indicate if the Legal Number should be enabled.  """  
      self.Rpt1DispInvoiceBal:int = obj["Rpt1DispInvoiceBal"]
      self.Rpt2DispInvoiceBal:int = obj["Rpt2DispInvoiceBal"]
      self.Rpt3DispInvoiceBal:int = obj["Rpt3DispInvoiceBal"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      """  GL Control description.  """  
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      """  GL Control Type description  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.TermsDescription:str = obj["TermsDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceLoadListTableset:
   def __init__(self, obj):
      self.APInvoiceLoadList:list[Erp_Tablesets_APInvoiceLoadListRow] = obj["APInvoiceLoadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvoiceLoadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenPayable:bool = obj["OpenPayable"]
      """  Indicates if this is an "open" Payable.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Vendor's invoice number.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      """   Indicates the type of document. Yes = Debit Memo,  No= Invoice. This value can't be changed after the record has been created.
Debit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign, but are entered as a positive.
The system uses this field to test for Debit Memos,  indicated by "DM" following the invoice number.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the PurTerms master file.  Defaulted from Vendor.TermsCode.  This is MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total sales tax amount for this invoice. Totals the TaxAmt from the APInvTax records of this invoice.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total sales tax amount for this invoice. Totals the DocTaxAmt from the APInvTax records of this invoice.  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Prompt payment discount due date. The date according to the terms when you are allowed to take the prompt payment discount (if any) given by the vendor. This date is NOT directly maintainable. It is calculated using the InvoiceDate + PurTerms.DiscountDays. If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then this is not applicable and is set to ? (null value).  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      """  Discount amount(Vendors Currency) that can be taken if paid by the DiscountDate.  This is calculated by the System via APInvHed write trigger. Formula ((PurTerms.DiscountPercent/100)*APInvHed.InvoiceBal on AIn.  If DebitMemo = Yes or PurTerms.NumberOfPayments > 1 then it is not applicable and is set to zero.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earliest unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts.(Vendors Currency) Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Bad name.  Actually this indicates if the invoice was created by the  open invoice load program.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the open payables file.    Only invoices that have been Posted (true) will be included as part of the open payables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related APInvGrp. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the APInvGrp or when the invoice date is changed.  It is overridable.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  This field represents the invoice # that this debit memo relates to. It can be left blank. If entered it must be a valid APInvHed record where the InvcHead.DebitMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the debit memos next to their corresponding invoice. Therefore, this field will always have a value.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall invoice.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount.(Vendors Currency) This field is an accumulation of the extended net amounts of the detail line items (APInvDtl) and of the miscellaneous charges/credits (APInvMsc) records.  This field has a true sign. (debit memos are negative).  """  
      self.DocInvoiceVendorAmt:int = obj["DocInvoiceVendorAmt"]
      """  A user entered verification amount.  DOCUMENT CURRENCY ONLY, a corresponding base currency field exists but is only used for external G/L interfacing.  This field is sign flipped for debit memos.  The calculated Invoice Amount (DocInvoiceAmt) must match this amount before the invoice can be posted.  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance.(Vendors currency)  Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts(Vendors currency). This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No. This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  This is NOT the same thing as putting an invoice on PaymentHold.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if this invoice should be held  from having any further payments made against it.  If "yes" then invoice  can't be selected in check processing.  """  
      self.Description:str = obj["Description"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.REFPONum:int = obj["REFPONum"]
      """  Reference PO number(optional when CM is present). Used to identify the PO that this Invoice is for.  If the Reference PO has a lock exchange rate then that is the rate that will be used on this AP  invoice,  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.UpdateTax:bool = obj["UpdateTax"]
      """  Controls the running of the Tax calculation logic which is found in the InvcHead write trigger.  """  
      self.InvoiceVendorAmt:int = obj["InvoiceVendorAmt"]
      """  For use by external G/L interfacing.  This field is sign flipped for debit memos.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identification of the Invoice.  """  
      self.FixedAmt:bool = obj["FixedAmt"]
      """  Allows user to control discount amount manually or automatically  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the invoice should be paid at the Central Payment Parent Company.  Used in Centralized Payment process.  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Flag to indicate if the invoice is linked from the source company invoice flagged for Central Payment.  """  
      self.CPayLegalNumber:str = obj["CPayLegalNumber"]
      """  This is the original Legal Number from the source invoice.  This is used in the Centralized Payment process.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  Reference Check number of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  Reference Check Date of the latest payment made by the Central Payment Parent Company for this invoice.  """  
      self.CPayInvoiceBal:int = obj["CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company. Carries a true sign. (Credit memos are negative).  """  
      self.CPayDocInvoiceBal:int = obj["CPayDocInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Vendors currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlType:str = obj["GLControlType"]
      """  The GL Control Type this invoice is assigned to.  This combined with GLControlCode links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to value 'APAcct'.  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  The GL Control Code this invoice is assigned to.  This combined with GLControlType links the invoice to a specific GLControl record which supplies the G/L account of the appropriate payables. Defaults to EntityGLC type of 'APAcct' assigned to the supplier.  """  
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceVendorAmt:int = obj["Rpt1InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceVendorAmt:int = obj["Rpt2InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceVendorAmt:int = obj["Rpt3InvoiceVendorAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Rpt1CPayInvoiceBal:int = obj["Rpt1CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt2CPayInvoiceBal:int = obj["Rpt2CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.Rpt3CPayInvoiceBal:int = obj["Rpt3CPayInvoiceBal"]
      """  Current outstanding balance of the corresponding invoice created at the Central Payment Parent Company (Report currency).  Carries a true sign. (Credit memos are negative).  """  
      self.AllowOverrideLI:bool = obj["AllowOverrideLI"]
      """  Identifies whether or not the amounts on a logged invoice can be overridden during AP Invoice Entry.  If set to false, the AP Invoice and Tax values must match the values on the Logged Invoice.  If set to true, the logged invoice is voided.  """  
      self.MatchedFromLI:bool = obj["MatchedFromLI"]
      """  Identifies if an invoice was matched from a logged invoice.  If yes, the invoice was matched.  If no, the invoice was not matched.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix is duplicated from the related APInvGrp. This is also refreshed if the ApplyDate is changed.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be set to Yes if the AP Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden and Finland Localization Field - Banking Reference  """  
      self.SEPayCode:str = obj["SEPayCode"]
      """  Sweden and Finland Localization Field - Payment Code  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is pre-payment invoice.  """  
      self.APLOCID:str = obj["APLOCID"]
      """  Letter of Credit ID.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.GUIImportTaxBasis:int = obj["GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis  """  
      self.DocGUIImportTaxBasis:int = obj["DocGUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in document currrency  """  
      self.Rpt1GUIImportTaxBasis:int = obj["Rpt1GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt1 currency  """  
      self.Rpt2GUIImportTaxBasis:int = obj["Rpt2GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt2 currency  """  
      self.Rpt3GUIImportTaxBasis:int = obj["Rpt3GUIImportTaxBasis"]
      """   Taiwan Localization
Tax Amount Basis in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked flag  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  The claim reference from the expense group that generated the invoice.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee from the group of expenses that created the invoice.  """  
      self.InBankFile:bool = obj["InBankFile"]
      """  Indicates that Invoice has been selected for payment in a bankfile  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Credit Note Confirmation Date  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.SelfLegalNumber:str = obj["SelfLegalNumber"]
      """  Legal Number for the self assessment.  """  
      self.SelfTranDocTypeID:str = obj["SelfTranDocTypeID"]
      """  Transaction Document Type for the self assessment.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.SupAgentName:str = obj["SupAgentName"]
      """  Supplier Agent Name  """  
      self.SupAgentTaxRegNo:str = obj["SupAgentTaxRegNo"]
      """  Supplier Agent Tax Region Number  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.NonDeductVATAmt:int = obj["NonDeductVATAmt"]
      """  Non Deductable VAT Amount  """  
      self.NonDeductVATDocAmt:int = obj["NonDeductVATDocAmt"]
      """  Non Deductable VAT Doc Amount  """  
      self.NonDeductVATRpt1Amt:int = obj["NonDeductVATRpt1Amt"]
      """  Non Deductable VAT Rpt1 Amount  """  
      self.NonDeductVATRpt2Amt:int = obj["NonDeductVATRpt2Amt"]
      """  Non Deductable VAT Rpt2 Amount  """  
      self.NonDeductVATRpt3Amt:int = obj["NonDeductVATRpt3Amt"]
      """  Non Deductable VAT Rpt3 Amount  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:str = obj["ImportedFrom"]
      """  Country of Import  """  
      self.ImportedDate:str = obj["ImportedDate"]
      """  Date of import.  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates that this is Advanced Tax invoice received from
supplier  """  
      self.InPrice:bool = obj["InPrice"]
      """   Indicates that the tax is included in the unit price
for this AP Invoice  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  In case of Tax Inclusive Pricing if system-calculated Header related taxes are changed/deleted/added  by the user - this field is set to true by the system.  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Assigned as "I" when Recurring Invoice has Inactive status.  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsMaxValue:bool = obj["IsMaxValue"]
      """  IsMaxValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.DMReason:str = obj["DMReason"]
      """  DMReason  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.AGDocPageNum:str = obj["AGDocPageNum"]
      """  AGDocPageNum  """  
      self.AGCAICAEMark:str = obj["AGCAICAEMark"]
      """  AGCAICAEMark  """  
      self.AGCAICAENum:str = obj["AGCAICAENum"]
      """  AGCAICAENum  """  
      self.AGCAICAEExpirationDate:str = obj["AGCAICAEExpirationDate"]
      """  AGCAICAEExpirationDate  """  
      self.AGAvTaxCreditFlag:bool = obj["AGAvTaxCreditFlag"]
      """  AGAvTaxCreditFlag  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGCustomsClearanceNum:str = obj["AGCustomsClearanceNum"]
      """  AGCustomsClearanceNum  """  
      self.AGCustomsCode:str = obj["AGCustomsCode"]
      """  AGCustomsCode  """  
      self.AGDestinationCode:str = obj["AGDestinationCode"]
      """  AGDestinationCode  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Header Number  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.TaxSvcID:str = obj["TaxSvcID"]
      """  'Type + - (OrderNum, InvoiceNum,  QuoteNum or TCDocID)'. Depending on the type, where Type is O=order, Q = quote, I = invoice, T=tax service doc ID (this is used to create an TaxSvcHead for tax reoconciliation when Tax Connect has a record with no corresponding Epicor record). Example: O-1234 is order type and order number 1234; Q-1234 is quote type and quote number 1234, etc.  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.APChkGrpID:str = obj["APChkGrpID"]
      """  AP Checking Group ID  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice Type  """  
      self.PEComputationalCost:str = obj["PEComputationalCost"]
      """  Indicates a computational cost for the invoice  """  
      self.ReferencedByBOE:str = obj["ReferencedByBOE"]
      """  Referenced By BOE  """  
      self.PEDUARefNum:str = obj["PEDUARefNum"]
      """  DUA Reference Number used on Peru Localiation  """  
      self.CustomsNumber:str = obj["CustomsNumber"]
      """  CustomsNumber  """  
      self.ReceivedDate:str = obj["ReceivedDate"]
      """  ReceivedDate  """  
      self.CustOverride:int = obj["CustOverride"]
      """  CustOverride  """  
      self.PrePaymentNum:str = obj["PrePaymentNum"]
      """  Invoice Number of Invoice Pre-Payment which should be automatically applied to this one during posting process.  """  
      self.PrePaymentAmt:int = obj["PrePaymentAmt"]
      """  Pre-Payment amount in Base Currency.  """  
      self.DocPrePaymentAmt:int = obj["DocPrePaymentAmt"]
      """  Pre-Payment amount in Document Currency.  """  
      self.Rpt1PrePaymentAmt:int = obj["Rpt1PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt2PrePaymentAmt:int = obj["Rpt2PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.Rpt3PrePaymentAmt:int = obj["Rpt3PrePaymentAmt"]
      """  Pre-Payment amount in Reporting Currency.  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  CSF Peru - AP Payment Number  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  SCF Peru - Detractions Tax Amount  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  Peru Detraction Tax Currency Code  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.DocPESUNATDepAmt:int = obj["DocPESUNATDepAmt"]
      """  Peru Document SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PESUNATNum:str = obj["PESUNATNum"]
      """  SUNAT Reference Number. Once a payment is made, the SUNAT returns a reference number used as the receipt number for the payment.  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  Document Tax Amount used in Peru detractions  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.PrePayHeadNum:int = obj["PrePayHeadNum"]
      """  PrePayHeadNum  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  Malaysia Import Declaration Number  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.GRNIClearing:bool = obj["GRNIClearing"]
      """  Flag that indicates if the invoice is a GRNI document.  """  
      self.PEFiscalCreditOperStatus:int = obj["PEFiscalCreditOperStatus"]
      """  CSF Peru - Fiscal Credit Operation Status  """  
      self.PEInternatTaxAgr:str = obj["PEInternatTaxAgr"]
      """  CSF Peru - International Tax agreement  """  
      self.PERentType:str = obj["PERentType"]
      """  CSF Peru - Rent type  """  
      self.PEPurchaseType:str = obj["PEPurchaseType"]
      """  CSF Peru - Purchase  type  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  TH Reference Invoice Num  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  TH Reference Vendor Num  """  
      self.JPSummarizationDate:str = obj["JPSummarizationDate"]
      """  Day when a company sums up accounts payable for supplier  """  
      self.JPBillingDate:str = obj["JPBillingDate"]
      """  Date of a Payment Statement  """  
      self.JPBillingNumber:str = obj["JPBillingNumber"]
      """  Legal Number of Payment Statement  """  
      self.SelfInvoice:bool = obj["SelfInvoice"]
      """  SelfInvoice  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.PurPoint:str = obj["PurPoint"]
      """  PurPoint  """  
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      """  PLInvoiceReference  """  
      self.INPortCode:str = obj["INPortCode"]
      """  INPortCode  """  
      self.RefCancelledby:str = obj["RefCancelledby"]
      """  Indicates which invoice number has cancelled this invoice.  """  
      self.CancellationInv:bool = obj["CancellationInv"]
      """  Indicates if this invoice is a cancellation invoice.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  Source Plant used for multi site GL  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.CHQRIBAN:str = obj["CHQRIBAN"]
      """  CHQRIBAN  """  
      self.CHQRReference:str = obj["CHQRReference"]
      """  CHQRReference  """  
      self.EDIInvoice:bool = obj["EDIInvoice"]
      """  Set to True for any invoice that is created via EDI  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.Code1099Description:str = obj["Code1099Description"]
      """  1099 Code Description, defaults from Supplier  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code, defaults from Supplier  """  
      self.DispInvoiceBal:int = obj["DispInvoiceBal"]
      """  Display field for Invoice Balance  """  
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      """  Form Type Description  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates whether created invoice should be paid.  """  
      self.PLVendorAutoInvoiceNum:bool = obj["PLVendorAutoInvoiceNum"]
      """  CSF Poland. Vendor uses Invoice reference number  """  
      self.Print1099:bool = obj["Print1099"]
      self.Rpt1DispInvoiceBal:int = obj["Rpt1DispInvoiceBal"]
      self.Rpt2DispInvoiceBal:int = obj["Rpt2DispInvoiceBal"]
      self.Rpt3DispInvoiceBal:int = obj["Rpt3DispInvoiceBal"]
      self.TaxableAmt1:int = obj["TaxableAmt1"]
      """  Taxable Value 1  """  
      self.TaxableAmt2:int = obj["TaxableAmt2"]
      """  Taxable Value 2  """  
      self.TaxableAmt3:int = obj["TaxableAmt3"]
      """  Taxable Value 3  """  
      self.TaxableAmt4:int = obj["TaxableAmt4"]
      """  Taxable Value 4  """  
      self.TaxAmt1:int = obj["TaxAmt1"]
      """  Tax Value 1  """  
      self.TaxAmt2:int = obj["TaxAmt2"]
      """  Tax Value 2  """  
      self.TaxAmt3:int = obj["TaxAmt3"]
      """  Tax Value 3  """  
      self.TaxAmt4:int = obj["TaxAmt4"]
      """  Tax Value 4  """  
      self.TaxCode1:str = obj["TaxCode1"]
      """  Tax Type 1  """  
      self.TaxCode1Description:str = obj["TaxCode1Description"]
      self.TaxCode2:str = obj["TaxCode2"]
      """  Tax Type 2  """  
      self.TaxCode2Description:str = obj["TaxCode2Description"]
      self.TaxCode3:str = obj["TaxCode3"]
      """  Tax Type 3  """  
      self.TaxCode3Description:str = obj["TaxCode3Description"]
      self.TaxCode4:str = obj["TaxCode4"]
      """  Tax Type 4  """  
      self.TaxCode4Description:str = obj["TaxCode4Description"]
      self.TaxRate1:str = obj["TaxRate1"]
      """  Tax Rate 1  """  
      self.TaxRate1Description:str = obj["TaxRate1Description"]
      self.TaxRate2:str = obj["TaxRate2"]
      """  Tax Rate 2  """  
      self.TaxRate2Description:str = obj["TaxRate2Description"]
      self.TaxRate3:str = obj["TaxRate3"]
      """  Tax Rate 3  """  
      self.TaxRate3Description:str = obj["TaxRate3Description"]
      self.TaxRate4:str = obj["TaxRate4"]
      """  Tax Rate 4  """  
      self.TaxRate4Description:str = obj["TaxRate4Description"]
      self.UseLegalNumber:bool = obj["UseLegalNumber"]
      """  Flag to indicate if the Legal Number should be enabled.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.BankName:str = obj["BankName"]
      self.DocDispInvoiceBal:int = obj["DocDispInvoiceBal"]
      """  Display field for DocInvoiceBal  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Site is a legal entity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.SourcePlantName:str = obj["SourcePlantName"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.VendorName:str = obj["VendorName"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorState:str = obj["VendorState"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.XbSystIsDiscountforDebitM:bool = obj["XbSystIsDiscountforDebitM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvoiceLoadTableset:
   def __init__(self, obj):
      self.APInvoiceLoad:list[Erp_Tablesets_APInvoiceLoadRow] = obj["APInvoiceLoad"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAPInvoiceLoadTableset:
   def __init__(self, obj):
      self.APInvoiceLoad:list[Erp_Tablesets_APInvoiceLoadRow] = obj["APInvoiceLoad"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["returnObj"]
      pass

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_APInvoiceLoadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPInvoiceLoad1_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class GetNewAPInvoiceLoad1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPInvoiceLoad_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewAPInvoiceLoad_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPInvoiceLoad
   whereClauseEntityGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPInvoiceLoad:str = obj["whereClauseAPInvoiceLoad"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaxTypesList_input:
   """ Required : 
   sTaxLiability
   """  
   def __init__(self, obj):
      self.sTaxLiability:str = obj["sTaxLiability"]
      """  Tax Liability.  """  
      pass

class GetTaxTypesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sTaxTypesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTotalBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTotalInvBal:int = obj["parameters"]
      self.opBaseCurrSymbol:str = obj["parameters"]
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

class OnChangeCurrencyCodeOrRateGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class OnChangeCurrencyCodeOrRateGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendBankID_input:
   """ Required : 
   vendorNum
   vendorBankID
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Bank ID  """  
      self.vendorBankID:str = obj["vendorBankID"]
      """  Vendor Bank ID  """  
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class OnChangeVendBankID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingInvoiceOrApplyDate_input:
   """ Required : 
   proposedDate
   dateField
   """  
   def __init__(self, obj):
      self.proposedDate:str = obj["proposedDate"]
      """  The proposed date  """  
      self.dateField:str = obj["dateField"]
      """  Pass "A' to check Apply Date or "I" for Invoice Date  """  
      pass

class OnChangingInvoiceOrApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dateMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangingTax_input:
   """ Required : 
   iTaxNum
   sTaxCode
   sTaxRate
   bCheckCollectionMethod
   ds
   """  
   def __init__(self, obj):
      self.iTaxNum:int = obj["iTaxNum"]
      """  Sequence number of tax (1 or 2 or 3)  """  
      self.sTaxCode:str = obj["sTaxCode"]
      """  Tax Code  """  
      self.sTaxRate:str = obj["sTaxRate"]
      """  Tax Rate  """  
      self.bCheckCollectionMethod:bool = obj["bCheckCollectionMethod"]
      """  Check tax type's collection method  """  
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class OnChangingTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostOpenInvLoad_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPInvoiceLoadTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPInvoiceLoadTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvoiceLoadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePLInvoiceReference_input:
   """ Required : 
   intVendorNum
   txtInvoiceNum
   txtPLInvoiceReference
   """  
   def __init__(self, obj):
      self.intVendorNum:int = obj["intVendorNum"]
      self.txtInvoiceNum:str = obj["txtInvoiceNum"]
      self.txtPLInvoiceReference:str = obj["txtPLInvoiceReference"]
      pass

class ValidatePLInvoiceReference_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isLogAPInvFound:bool = obj["isLogAPInvFound"]
      self.logAPInvNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateVendorID_input:
   """ Required : 
   vendorID
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      pass

class ValidateVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vendorNum:int = obj["parameters"]
      pass

      """  output parameters  """  

