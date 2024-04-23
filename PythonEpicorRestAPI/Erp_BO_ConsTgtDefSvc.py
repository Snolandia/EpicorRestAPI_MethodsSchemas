import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConsTgtDefSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtDefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs",headers=creds) as resp:
           return await resp.json()

async def post_ConsTgtDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtDef item
   Description: Calls GetByID to retrieve the ConsTgtDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsTgtDef for the service
   Description: Calls UpdateExt to update ConsTgtDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsTgtDef item
   Description: Call UpdateExt to delete ConsTgtDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs(Company, ConsDefID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsTgtSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtSrcs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtSrcs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtSrcs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs",headers=creds) as resp:
           return await resp.json()

async def post_ConsTgtSrcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsTgtSrc for the service
   Description: Calls UpdateExt to update ConsTgtSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsTgtSrc item
   Description: Call UpdateExt to delete ConsTgtSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseConsTgtDef, whereClauseConsTgtSrc, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseConsTgtDef=" + whereClauseConsTgtDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsTgtSrc=" + whereClauseConsTgtSrc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(consDefID, epicorHeaders = None):
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
   params += "consDefID=" + consDefID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOAMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOAMap
   Description: Purpose:
Parameters:
<param name="ipCOAMapUID">COA Map ID to validate</param><param name="ipSourceCOA">COA for the Source Book</param><param name="ipTargetCOA">COA for the Intermediate Book if any</param>
Notes:
   OperationID: CheckCOAMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOAMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOAMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConsolidationType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConsolidationType
   Description: Purpose:
Parameters:
<param name="ipConsolidationType">proposed consolidation type (Periodic/Continuous)</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckConsolidationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConsolidationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsolidationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConsType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConsType
   Description: Purpose:
Parameters:
<param name="ipConsType">ConsType to edit</param><param name="ipConsTypeText">text that identifies the constype being validated</param>
Notes:
   OperationID: CheckConsType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConsType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrencyCode
   Description: Purpose:
Parameters:
<param name="ipCurrencyCode">currency code to validate</param>
Notes:
   OperationID: CheckCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIfResetTgtBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIfResetTgtBook
   Description: Purpose:
Parameters:
<param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckIfResetTgtBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfResetTgtBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfResetTgtBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIntermediateBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIntermediateBook
   Description: Purpose:
Parameters:
<param name="ipIntermediateBook">IntermediateBookID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckIntermediateBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIntermediateBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIntermediateBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckJournalCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckJournalCode
   Description: Purpose:
Parameters:
<param name="ipJrnlCode">Journal code to edit</param><param name="ipJrnlCodeType">Identifies which journal code to edit: target or intermediate</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckJournalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOutputFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOutputFile
   Description: Purpose:  Verify the outputfile is unqique
Parameters:
<param name="ipOutputFile">output file</param>
Notes:
   OperationID: CheckOutputFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOutputFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOutputFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRemoteParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRemoteParent
   Description: Purpose:
Parameters:
<param name="ipRemoteParent">remote parent value</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckRemoteParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRemoteParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRemoteParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTargetBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTargetBook
   Description: Purpose:
Parameters:
<param name="ipTargetBook">target book ID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckTargetBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTargetBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTargetBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTargetCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTargetCompany
   Description: Purpose:
Parameters:
<param name="ipTargetCompany">target Company ID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: CheckTargetCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTargetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTargetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSourceCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSourceCOA
   Description: Purpose:  Updates the Source COA when the Source Book changes
Parameters:
<param name="ipSourceBook">Source GL Book ID</param><param name="ds">Consolidation targetDefinition Data Set</param>
Notes:
   OperationID: GetSourceCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourceCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsSourceBookDefined(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsSourceBookDefined
   Description: Purpose:  Checks to see if the source book is already defined for this ConsDefID
Parameters:
<param name="ipConsDefID">Consolidation Definition ID</param><param name="ipSourceBook">Source GL Book ID</param>
Notes:
   OperationID: IsSourceBookDefined
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsSourceBookDefined_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsSourceBookDefined_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getCompaniesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getCompaniesList
   Description: To get external companies configured for current company.
   OperationID: getCompaniesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getCompaniesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getCompaniesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAdd
   Description: Check if account is valid and set description for it
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForTargetBookCmb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForTargetBookCmb
   Description: Generates list of available target books in string format.
   OperationID: GetListForTargetBookCmb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForTargetBookCmb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTargetBookCmb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForTargetJrnlCmb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForTargetJrnlCmb
   Description: Generates list of available target journals in string format.
   OperationID: GetListForTargetJrnlCmb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForTargetJrnlCmb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForTargetJrnlCmb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForCOAMapUIDCmb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForCOAMapUIDCmb
   Description: Returns list of available COA Mappings
   OperationID: GetListForCOAMapUIDCmb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForCOAMapUIDCmb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForCOAMapUIDCmb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConsolidationTypeOnChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConsolidationTypeOnChanging
   Description: ConsolidationType Column changing.
   OperationID: ConsolidationTypeOnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConsolidationTypeOnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConsolidationTypeOnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsTgtDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsTgtDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsTgtSrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsTgtSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsTgtDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtSrcRow] = obj["value"]
      pass

class Erp_Tablesets_ConsTgtDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TgtBookCal:str = obj["TgtBookCal"]
      """  Target Book Fiscal Calendar  """  
      self.IterBookFiscalCal:str = obj["IterBookFiscalCal"]
      """  Intermediate book fiscal calendar  """  
      self.TgtBookFiscalCal:str = obj["TgtBookFiscalCal"]
      """  Target Book fiscal Calendar  """  
      self.TgtBookDesc:str = obj["TgtBookDesc"]
      """  Target Book Description  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.InterBookDescription:str = obj["InterBookDescription"]
      """  Descripiton of Book  """  
      self.InterBookCurrencyCode:str = obj["InterBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.TargetCOName:str = obj["TargetCOName"]
      """  Company Name  """  
      self.TgtCOADescription:str = obj["TgtCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TgtCurrencyCurrencyID:str = obj["TgtCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.TgtCurrencyDocumentDesc:str = obj["TgtCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.TgtCurrencyCurrName:str = obj["TgtCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.TgtCurrencyCurrDesc:str = obj["TgtCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.TgtCurrencyCurrSymbol:str = obj["TgtCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TgtBookCal:str = obj["TgtBookCal"]
      """  Target Book Fiscal Calendar  """  
      self.IterBookFiscalCal:str = obj["IterBookFiscalCal"]
      """  Intermediate book fiscal calendar  """  
      self.TgtBookFiscalCal:str = obj["TgtBookFiscalCal"]
      """  Target Book fiscal Calendar  """  
      self.TgtBookDesc:str = obj["TgtBookDesc"]
      """  Target Book Description  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.AdjustModeInput:bool = obj["AdjustModeInput"]
      """  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company  """  
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      """  Source Company Name  """  
      self.HasConsolitation:bool = obj["HasConsolitation"]
      """  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  """  
      self.LastGenStatus:str = obj["LastGenStatus"]
      """  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  """  
      self.IterBookFiscalCalID:str = obj["IterBookFiscalCalID"]
      """  Intermediate book fiscal calendar ID.  """  
      self.TgtBookFiscalCalID:str = obj["TgtBookFiscalCalID"]
      """  Target Book fiscal Calendar ID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InterBookCurrencyCode:str = obj["InterBookCurrencyCode"]
      self.InterBookDescription:str = obj["InterBookDescription"]
      self.TargetCOName:str = obj["TargetCOName"]
      self.TgtCOADescription:str = obj["TgtCOADescription"]
      self.TgtCurrencyCurrName:str = obj["TgtCurrencyCurrName"]
      self.TgtCurrencyCurrSymbol:str = obj["TgtCurrencyCurrSymbol"]
      self.TgtCurrencyCurrencyID:str = obj["TgtCurrencyCurrencyID"]
      self.TgtCurrencyDocumentDesc:str = obj["TgtCurrencyDocumentDesc"]
      self.TgtCurrencyCurrDesc:str = obj["TgtCurrencyCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.BalanceSheetDefType:str = obj["BalanceSheetDefType"]
      """  The related ConsType ID  """  
      self.IncomeStmtDefType:str = obj["IncomeStmtDefType"]
      """  The related ConsType ID  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  """  
      self.ExcludeOpenPrds:bool = obj["ExcludeOpenPrds"]
      """  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  """  
      self.TgtJrnlCode:str = obj["TgtJrnlCode"]
      """  The journal code to use when posting the consolidation records in the target company book.  """  
      self.ReverseDBCR:bool = obj["ReverseDBCR"]
      """  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  """  
      self.IntermediateJrnlCode:str = obj["IntermediateJrnlCode"]
      """  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  """  
      self.DiffOnExchangeAcct:str = obj["DiffOnExchangeAcct"]
      """  Account Number where rounding differences will be posted  """  
      self.DiffExSegValue1:str = obj["DiffExSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue2:str = obj["DiffExSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue3:str = obj["DiffExSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.DiffExSegValue4:str = obj["DiffExSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.DiffExSegValue5:str = obj["DiffExSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.DiffExSegValue6:str = obj["DiffExSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.DiffExSegValue7:str = obj["DiffExSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.DiffExSegValue8:str = obj["DiffExSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.DiffExSegValue9:str = obj["DiffExSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.DiffExSegValue10:str = obj["DiffExSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.DiffExSegValue11:str = obj["DiffExSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.DiffExSegValue12:str = obj["DiffExSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.DiffExSegValue13:str = obj["DiffExSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.DiffExSegValue14:str = obj["DiffExSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.DiffExSegValue15:str = obj["DiffExSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.DiffExSegValue16:str = obj["DiffExSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.DiffExSegValue17:str = obj["DiffExSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.DiffExSegValue18:str = obj["DiffExSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.DiffExSegValue19:str = obj["DiffExSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.DiffExSegValue20:str = obj["DiffExSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target COA - this field is intended for internal use  """  
      self.TargetCompany:str = obj["TargetCompany"]
      """  Target Company ID - intended for internal use  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source COA code  """  
      self.InterJrnlDesc:str = obj["InterJrnlDesc"]
      """  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.TgtJrnlCodeDesc:str = obj["TgtJrnlCodeDesc"]
      """  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      """  Currency code description from either the Currency or GLBCurrency table.  """  
      self.SrcFiscalCalendar:str = obj["SrcFiscalCalendar"]
      """  Source book fiscal calendar.  """  
      self.DiffOnExchangeDesc:str = obj["DiffOnExchangeDesc"]
      """  Holds GLAccount description temporarily to provide extra information to the user.  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BalanceConsTypeDescription:str = obj["BalanceConsTypeDescription"]
      self.BalanceRateDescription:str = obj["BalanceRateDescription"]
      self.COAMapDisplayName:str = obj["COAMapDisplayName"]
      self.IncomeConsTypeDescription:str = obj["IncomeConsTypeDescription"]
      self.IncomeRateDescription:str = obj["IncomeRateDescription"]
      self.SrcBookDescription:str = obj["SrcBookDescription"]
      self.SrcBookCurrencyCode:str = obj["SrcBookCurrencyCode"]
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckCOAMap_input:
   """ Required : 
   ipCOAMapUID
   ipSourceCOA
   ipTargetCOA
   """  
   def __init__(self, obj):
      self.ipCOAMapUID:int = obj["ipCOAMapUID"]
      self.ipSourceCOA:str = obj["ipSourceCOA"]
      self.ipTargetCOA:str = obj["ipTargetCOA"]
      pass

class CheckCOAMap_output:
   def __init__(self, obj):
      pass

class CheckConsType_input:
   """ Required : 
   ipConsType
   ipConsTypeText
   """  
   def __init__(self, obj):
      self.ipConsType:str = obj["ipConsType"]
      self.ipConsTypeText:str = obj["ipConsTypeText"]
      pass

class CheckConsType_output:
   def __init__(self, obj):
      pass

class CheckConsolidationType_input:
   """ Required : 
   ipConsolidationType
   ds
   """  
   def __init__(self, obj):
      self.ipConsolidationType:str = obj["ipConsolidationType"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckConsolidationType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCurrencyCode_input:
   """ Required : 
   ipCurrencyCode
   """  
   def __init__(self, obj):
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      pass

class CheckCurrencyCode_output:
   def __init__(self, obj):
      pass

class CheckIfResetTgtBook_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckIfResetTgtBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckIntermediateBook_input:
   """ Required : 
   ipIntermediateBook
   ds
   """  
   def __init__(self, obj):
      self.ipIntermediateBook:str = obj["ipIntermediateBook"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckIntermediateBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckJournalCode_input:
   """ Required : 
   ipJrnlCode
   ipJrnlCodeType
   ds
   """  
   def __init__(self, obj):
      self.ipJrnlCode:str = obj["ipJrnlCode"]
      self.ipJrnlCodeType:str = obj["ipJrnlCodeType"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckJournalCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckOutputFile_input:
   """ Required : 
   ipOutputFile
   """  
   def __init__(self, obj):
      self.ipOutputFile:str = obj["ipOutputFile"]
      pass

class CheckOutputFile_output:
   def __init__(self, obj):
      pass

class CheckRemoteParent_input:
   """ Required : 
   ipRemoteParent
   ds
   """  
   def __init__(self, obj):
      self.ipRemoteParent:bool = obj["ipRemoteParent"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckRemoteParent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTargetBook_input:
   """ Required : 
   ipTargetBook
   ds
   """  
   def __init__(self, obj):
      self.ipTargetBook:str = obj["ipTargetBook"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckTargetBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTargetCompany_input:
   """ Required : 
   ipTargetCompany
   ds
   """  
   def __init__(self, obj):
      self.ipTargetCompany:str = obj["ipTargetCompany"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class CheckTargetCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConsolidationTypeOnChanging_input:
   """ Required : 
   ipConsolidationType
   ds
   """  
   def __init__(self, obj):
      self.ipConsolidationType:str = obj["ipConsolidationType"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class ConsolidationTypeOnChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultsOnAdd_input:
   """ Required : 
   glAccount
   ds
   """  
   def __init__(self, obj):
      self.glAccount:str = obj["glAccount"]
      """  GL Account being processed  """  
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class DefaultsOnAdd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   consDefID
   """  
   def __init__(self, obj):
      self.consDefID:str = obj["consDefID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ConsTgtDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TgtBookCal:str = obj["TgtBookCal"]
      """  Target Book Fiscal Calendar  """  
      self.IterBookFiscalCal:str = obj["IterBookFiscalCal"]
      """  Intermediate book fiscal calendar  """  
      self.TgtBookFiscalCal:str = obj["TgtBookFiscalCal"]
      """  Target Book fiscal Calendar  """  
      self.TgtBookDesc:str = obj["TgtBookDesc"]
      """  Target Book Description  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.InterBookDescription:str = obj["InterBookDescription"]
      """  Descripiton of Book  """  
      self.InterBookCurrencyCode:str = obj["InterBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.TargetCOName:str = obj["TargetCOName"]
      """  Company Name  """  
      self.TgtCOADescription:str = obj["TgtCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TgtCurrencyCurrencyID:str = obj["TgtCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.TgtCurrencyDocumentDesc:str = obj["TgtCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.TgtCurrencyCurrName:str = obj["TgtCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.TgtCurrencyCurrDesc:str = obj["TgtCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.TgtCurrencyCurrSymbol:str = obj["TgtCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtDefListTableset:
   def __init__(self, obj):
      self.ConsTgtDefList:list[Erp_Tablesets_ConsTgtDefListRow] = obj["ConsTgtDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConsTgtDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TgtBookCal:str = obj["TgtBookCal"]
      """  Target Book Fiscal Calendar  """  
      self.IterBookFiscalCal:str = obj["IterBookFiscalCal"]
      """  Intermediate book fiscal calendar  """  
      self.TgtBookFiscalCal:str = obj["TgtBookFiscalCal"]
      """  Target Book fiscal Calendar  """  
      self.TgtBookDesc:str = obj["TgtBookDesc"]
      """  Target Book Description  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.AdjustModeInput:bool = obj["AdjustModeInput"]
      """  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company  """  
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      """  Source Company Name  """  
      self.HasConsolitation:bool = obj["HasConsolitation"]
      """  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  """  
      self.LastGenStatus:str = obj["LastGenStatus"]
      """  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  """  
      self.IterBookFiscalCalID:str = obj["IterBookFiscalCalID"]
      """  Intermediate book fiscal calendar ID.  """  
      self.TgtBookFiscalCalID:str = obj["TgtBookFiscalCalID"]
      """  Target Book fiscal Calendar ID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InterBookCurrencyCode:str = obj["InterBookCurrencyCode"]
      self.InterBookDescription:str = obj["InterBookDescription"]
      self.TargetCOName:str = obj["TargetCOName"]
      self.TgtCOADescription:str = obj["TgtCOADescription"]
      self.TgtCurrencyCurrName:str = obj["TgtCurrencyCurrName"]
      self.TgtCurrencyCurrSymbol:str = obj["TgtCurrencyCurrSymbol"]
      self.TgtCurrencyCurrencyID:str = obj["TgtCurrencyCurrencyID"]
      self.TgtCurrencyDocumentDesc:str = obj["TgtCurrencyDocumentDesc"]
      self.TgtCurrencyCurrDesc:str = obj["TgtCurrencyCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtDefTableset:
   def __init__(self, obj):
      self.ConsTgtDef:list[Erp_Tablesets_ConsTgtDefRow] = obj["ConsTgtDef"]
      self.ConsTgtSrc:list[Erp_Tablesets_ConsTgtSrcRow] = obj["ConsTgtSrc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConsTgtSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.BalanceSheetDefType:str = obj["BalanceSheetDefType"]
      """  The related ConsType ID  """  
      self.IncomeStmtDefType:str = obj["IncomeStmtDefType"]
      """  The related ConsType ID  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  """  
      self.ExcludeOpenPrds:bool = obj["ExcludeOpenPrds"]
      """  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  """  
      self.TgtJrnlCode:str = obj["TgtJrnlCode"]
      """  The journal code to use when posting the consolidation records in the target company book.  """  
      self.ReverseDBCR:bool = obj["ReverseDBCR"]
      """  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  """  
      self.IntermediateJrnlCode:str = obj["IntermediateJrnlCode"]
      """  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  """  
      self.DiffOnExchangeAcct:str = obj["DiffOnExchangeAcct"]
      """  Account Number where rounding differences will be posted  """  
      self.DiffExSegValue1:str = obj["DiffExSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue2:str = obj["DiffExSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue3:str = obj["DiffExSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.DiffExSegValue4:str = obj["DiffExSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.DiffExSegValue5:str = obj["DiffExSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.DiffExSegValue6:str = obj["DiffExSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.DiffExSegValue7:str = obj["DiffExSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.DiffExSegValue8:str = obj["DiffExSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.DiffExSegValue9:str = obj["DiffExSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.DiffExSegValue10:str = obj["DiffExSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.DiffExSegValue11:str = obj["DiffExSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.DiffExSegValue12:str = obj["DiffExSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.DiffExSegValue13:str = obj["DiffExSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.DiffExSegValue14:str = obj["DiffExSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.DiffExSegValue15:str = obj["DiffExSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.DiffExSegValue16:str = obj["DiffExSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.DiffExSegValue17:str = obj["DiffExSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.DiffExSegValue18:str = obj["DiffExSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.DiffExSegValue19:str = obj["DiffExSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.DiffExSegValue20:str = obj["DiffExSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target COA - this field is intended for internal use  """  
      self.TargetCompany:str = obj["TargetCompany"]
      """  Target Company ID - intended for internal use  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source COA code  """  
      self.InterJrnlDesc:str = obj["InterJrnlDesc"]
      """  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.TgtJrnlCodeDesc:str = obj["TgtJrnlCodeDesc"]
      """  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      """  Currency code description from either the Currency or GLBCurrency table.  """  
      self.SrcFiscalCalendar:str = obj["SrcFiscalCalendar"]
      """  Source book fiscal calendar.  """  
      self.DiffOnExchangeDesc:str = obj["DiffOnExchangeDesc"]
      """  Holds GLAccount description temporarily to provide extra information to the user.  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BalanceConsTypeDescription:str = obj["BalanceConsTypeDescription"]
      self.BalanceRateDescription:str = obj["BalanceRateDescription"]
      self.COAMapDisplayName:str = obj["COAMapDisplayName"]
      self.IncomeConsTypeDescription:str = obj["IncomeConsTypeDescription"]
      self.IncomeRateDescription:str = obj["IncomeRateDescription"]
      self.SrcBookDescription:str = obj["SrcBookDescription"]
      self.SrcBookCurrencyCode:str = obj["SrcBookCurrencyCode"]
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConsTgtDefTableset:
   def __init__(self, obj):
      self.ConsTgtDef:list[Erp_Tablesets_ConsTgtDefRow] = obj["ConsTgtDef"]
      self.ConsTgtSrc:list[Erp_Tablesets_ConsTgtSrcRow] = obj["ConsTgtSrc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   consDefID
   """  
   def __init__(self, obj):
      self.consDefID:str = obj["consDefID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsTgtDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsTgtDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsTgtDefTableset] = obj["returnObj"]
      pass

class GetListForCOAMapUIDCmb_input:
   """ Required : 
   ipConsDefID
   ipSourceCOA
   """  
   def __init__(self, obj):
      self.ipConsDefID:str = obj["ipConsDefID"]
      self.ipSourceCOA:str = obj["ipSourceCOA"]
      pass

class GetListForCOAMapUIDCmb_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListForTargetBookCmb_input:
   """ Required : 
   ipCompany
   ipTgtCompany
   ipExtCompany
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipTgtCompany:str = obj["ipTgtCompany"]
      self.ipExtCompany:str = obj["ipExtCompany"]
      pass

class GetListForTargetBookCmb_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListForTargetJrnlCmb_input:
   """ Required : 
   ipCompany
   ipTgtCompany
   ipExtCompany
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipTgtCompany:str = obj["ipTgtCompany"]
      self.ipExtCompany:str = obj["ipExtCompany"]
      pass

class GetListForTargetJrnlCmb_output:
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
      self.returnObj:list[Erp_Tablesets_ConsTgtDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewConsTgtDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class GetNewConsTgtDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsTgtSrc_input:
   """ Required : 
   ds
   consDefID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      self.consDefID:str = obj["consDefID"]
      pass

class GetNewConsTgtSrc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseConsTgtDef
   whereClauseConsTgtSrc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseConsTgtDef:str = obj["whereClauseConsTgtDef"]
      self.whereClauseConsTgtSrc:str = obj["whereClauseConsTgtSrc"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsTgtDefTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSourceCOA_input:
   """ Required : 
   ipSourceBook
   ds
   """  
   def __init__(self, obj):
      self.ipSourceBook:str = obj["ipSourceBook"]
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class GetSourceCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
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

class IsSourceBookDefined_input:
   """ Required : 
   ipConsDefID
   ipSourceBook
   """  
   def __init__(self, obj):
      self.ipConsDefID:str = obj["ipConsDefID"]
      self.ipSourceBook:str = obj["ipSourceBook"]
      pass

class IsSourceBookDefined_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConsTgtDefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConsTgtDefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsTgtDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class getCompaniesList_input:
   """ Required : 
   consTypeSelected
   """  
   def __init__(self, obj):
      self.consTypeSelected:str = obj["consTypeSelected"]
      pass

class getCompaniesList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  String  """  
      pass

