import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DataFixSvc
# Description: DataFix functionality
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataFixes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.datafixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes",headers=creds) as resp:
           return await resp.json()

async def post_DataFixes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.datafixRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.datafixRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFix item
   Description: Calls GetByID to retrieve the DataFix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.datafixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataFix for the service
   Description: Calls UpdateExt to update DataFix. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.datafixRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataFix item
   Description: Call UpdateExt to delete DataFix item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixDDefs(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataFixDDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataFixDDefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixDDefs",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFixDDef item
   Description: Calls GetByID to retrieve the DataFixDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixDDef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixParams(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataFixParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataFixParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixParams",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFixParam item
   Description: Calls GetByID to retrieve the DataFixParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixRpts(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DataFixRpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataFixRpts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixRpts",headers=creds) as resp:
           return await resp.json()

async def get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFixRpt item
   Description: Calls GetByID to retrieve the DataFixRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixRpt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataFixDDefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataFixDDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixDDefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs",headers=creds) as resp:
           return await resp.json()

async def post_DataFixDDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixDDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFixDDef item
   Description: Calls GetByID to retrieve the DataFixDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixDDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataFixDDef for the service
   Description: Calls UpdateExt to update DataFixDDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFixDDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tabseq, tblname, seqnum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataFixDDef item
   Description: Call UpdateExt to delete DataFixDDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFixDDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tabseq: Desc: tabseq   Required: True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqnum: Desc: seqnum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataFixParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataFixParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams",headers=creds) as resp:
           return await resp.json()

async def post_DataFixParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFixParam item
   Description: Calls GetByID to retrieve the DataFixParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataFixParam for the service
   Description: Calls UpdateExt to update DataFixParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFixParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company, LocalName, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataFixParam item
   Description: Call UpdateExt to delete DataFixParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFixParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_DataFixRpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DataFixRpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixRpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts",headers=creds) as resp:
           return await resp.json()

async def post_DataFixRpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixRpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DataFixRpt item
   Description: Calls GetByID to retrieve the DataFixRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixRpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DataFixRpt for the service
   Description: Calls UpdateExt to update DataFixRpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFixRpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company, LocalName, Key1, Key2, Key3, Key4, Key5, tblname, seqId, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DataFixRpt item
   Description: Call UpdateExt to delete DataFixRpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFixRpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param tblname: Desc: tblname   Required: True   Allow empty value : True
      :param seqId: Desc: seqId   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.datafixlistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausedatafix, whereClauseDataFixDDef, whereClauseDataFixParam, whereClauseDataFixRpt, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClausedatafix=" + whereClausedatafix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataFixDDef=" + whereClauseDataFixDDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataFixParam=" + whereClauseDataFixParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDataFixRpt=" + whereClauseDataFixRpt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, localName, key1, key2, key3, key4, key5, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "localName=" + localName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key4=" + key4
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key5=" + key5

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDCustom
   Description: Get DataFix data for given DataFixId
   OperationID: GetByIDCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Retrieve DataFix rows from Local001 table and populate temp tables
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartReport
   Description: Start Report
   OperationID: StartReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateReport
   Description: Update Report
   OperationID: UpdateReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelReport
   Description: Cancel Report
   OperationID: CancelReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReport
   Description: Get Report
   OperationID: GetReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportSysRowIDUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportSysRowIDUpdate
   Description: Get Report
   OperationID: GetReportSysRowIDUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportSysRowIDUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportSysRowIDUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetFix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetFix
   Description: Reset a Fix parameters and clear report
   OperationID: ResetFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectAll
   Description: Select all the current report records
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnSelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnSelectAll
   Description: UnSelect all the current report records
   OperationID: UnSelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnSelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnSelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnQuote
   Description: remove quotes from a string
   OperationID: UnQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunUpdate
   Description: Run Data Fix Update
   OperationID: RunUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunUpdateNoDisplay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunUpdateNoDisplay
   Description: Run Data Fix Update without displaying data first
   OperationID: RunUpdateNoDisplay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunUpdateNoDisplay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunUpdateNoDisplay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTenants(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTenants
   Description: Get Tenants
   OperationID: GetTenants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTenants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTenants_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentTenantID(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentTenantID
   Description: Get Current Tenant ID
   OperationID: GetCurrentTenantID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetInstallationID(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstallationID
   Description: Get Installation ID
   OperationID: GetInstallationID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstallationID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentInstallationID(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentInstallationID
   Description: Get Current Tenant ID
   OperationID: GetCurrentInstallationID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentInstallationID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ImportDataFix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportDataFix
   Description: Import a new data fix
   OperationID: ImportDataFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDataFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDataFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrereadDataFix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrereadDataFix
   OperationID: PrereadDataFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrereadDataFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrereadDataFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateParameterComponents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateParameterComponents
   Description: Generate the necessary components to fill parameters from ds.
   OperationID: GenerateParameterComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateParameterComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateParameterComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanies(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanies
   Description: Get the companies available.
   OperationID: GetCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UploadLocalImportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadLocalImportFile
   OperationID: UploadLocalImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadLocalImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadLocalImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsDataFix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsDataFix
   Description: Retrieve DataFix rows from Local001 table and populate temp tables
   OperationID: GetRowsDataFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsDataFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsDataFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewdatafix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewdatafix
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewdatafix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewdatafix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewdatafix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixDDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataFixDDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataFixParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixRptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DataFixRptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_datafixRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixlistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_datafixlistRow] = obj["value"]
      pass

class Erp_Tablesets_DataFixDDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.seqnum:int = obj["seqnum"]
      self.datafixddefid:str = obj["datafixddefid"]
      self.tblname:str = obj["tblname"]
      self.colname:str = obj["colname"]
      self.width:int = obj["width"]
      self.datatype:str = obj["datatype"]
      self.tabseq:int = obj["tabseq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataFixParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.Label01:str = obj["Label01"]
      self.Value01:str = obj["Value01"]
      self.BlankOK01:bool = obj["BlankOK01"]
      self.DataType01:str = obj["DataType01"]
      self.ViewType01:str = obj["ViewType01"]
      self.Label02:str = obj["Label02"]
      self.Value02:str = obj["Value02"]
      self.BlankOK02:bool = obj["BlankOK02"]
      self.DataType02:str = obj["DataType02"]
      self.ViewType02:str = obj["ViewType02"]
      self.Label03:str = obj["Label03"]
      self.Value03:str = obj["Value03"]
      self.BlankOK03:bool = obj["BlankOK03"]
      self.DataType03:str = obj["DataType03"]
      self.ViewType03:str = obj["ViewType03"]
      self.Label04:str = obj["Label04"]
      self.Value04:str = obj["Value04"]
      self.BlankOK04:bool = obj["BlankOK04"]
      self.DataType04:str = obj["DataType04"]
      self.ViewType04:str = obj["ViewType04"]
      self.Label05:str = obj["Label05"]
      self.Value05:str = obj["Value05"]
      self.BlankOK05:bool = obj["BlankOK05"]
      self.DataType05:str = obj["DataType05"]
      self.ViewType05:str = obj["ViewType05"]
      self.Label06:str = obj["Label06"]
      self.Value06:str = obj["Value06"]
      self.BlankOK06:bool = obj["BlankOK06"]
      self.DataType06:str = obj["DataType06"]
      self.ViewType06:str = obj["ViewType06"]
      self.Label07:str = obj["Label07"]
      self.Value07:str = obj["Value07"]
      self.BlankOK07:bool = obj["BlankOK07"]
      self.DataType07:str = obj["DataType07"]
      self.ViewType07:str = obj["ViewType07"]
      self.Label08:str = obj["Label08"]
      self.Value08:str = obj["Value08"]
      self.BlankOK08:bool = obj["BlankOK08"]
      self.DataType08:str = obj["DataType08"]
      self.ViewType08:str = obj["ViewType08"]
      self.Label09:str = obj["Label09"]
      self.Value09:str = obj["Value09"]
      self.BlankOK09:bool = obj["BlankOK09"]
      self.DataType09:str = obj["DataType09"]
      self.ViewType09:str = obj["ViewType09"]
      self.Label10:str = obj["Label10"]
      self.Value10:str = obj["Value10"]
      self.BlankOK10:bool = obj["BlankOK10"]
      self.DataType10:str = obj["DataType10"]
      self.ViewType10:str = obj["ViewType10"]
      self.Label11:str = obj["Label11"]
      self.Value11:str = obj["Value11"]
      self.BlankOK11:bool = obj["BlankOK11"]
      self.DataType11:str = obj["DataType11"]
      self.ViewType11:str = obj["ViewType11"]
      self.Label12:str = obj["Label12"]
      self.Value12:str = obj["Value12"]
      self.BlankOK12:bool = obj["BlankOK12"]
      self.DataType12:str = obj["DataType12"]
      self.ViewType12:str = obj["ViewType12"]
      self.Label13:str = obj["Label13"]
      self.Value13:str = obj["Value13"]
      self.BlankOK13:bool = obj["BlankOK13"]
      self.DataType13:str = obj["DataType13"]
      self.ViewType13:str = obj["ViewType13"]
      self.Label14:str = obj["Label14"]
      self.Value14:str = obj["Value14"]
      self.BlankOK14:bool = obj["BlankOK14"]
      self.DataType14:str = obj["DataType14"]
      self.ViewType14:str = obj["ViewType14"]
      self.Label15:str = obj["Label15"]
      self.Value15:str = obj["Value15"]
      self.BlankOK15:bool = obj["BlankOK15"]
      self.DataType15:str = obj["DataType15"]
      self.ViewType15:str = obj["ViewType15"]
      self.Label16:str = obj["Label16"]
      self.Value16:str = obj["Value16"]
      self.BlankOK16:bool = obj["BlankOK16"]
      self.DataType16:str = obj["DataType16"]
      self.ViewType16:str = obj["ViewType16"]
      self.Label17:str = obj["Label17"]
      self.Value17:str = obj["Value17"]
      self.BlankOK17:bool = obj["BlankOK17"]
      self.DataType17:str = obj["DataType17"]
      self.ViewType17:str = obj["ViewType17"]
      self.Label18:str = obj["Label18"]
      self.Value18:str = obj["Value18"]
      self.BlankOK18:bool = obj["BlankOK18"]
      self.DataType18:str = obj["DataType18"]
      self.ViewType18:str = obj["ViewType18"]
      self.Label19:str = obj["Label19"]
      self.Value19:str = obj["Value19"]
      self.BlankOK19:bool = obj["BlankOK19"]
      self.DataType19:str = obj["DataType19"]
      self.ViewType19:str = obj["ViewType19"]
      self.Label20:str = obj["Label20"]
      self.Value20:str = obj["Value20"]
      self.BlankOK20:bool = obj["BlankOK20"]
      self.DataType20:str = obj["DataType20"]
      self.ViewType20:str = obj["ViewType20"]
      self.BlankCompOK:bool = obj["BlankCompOK"]
      self.LabelComp:str = obj["LabelComp"]
      self.ViewTypeComp:str = obj["ViewTypeComp"]
      self.ValueComp:str = obj["ValueComp"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataFixRptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.UpdInd:bool = obj["UpdInd"]
      self.UpdTable:str = obj["UpdTable"]
      self.value01:str = obj["value01"]
      self.value02:str = obj["value02"]
      self.value03:str = obj["value03"]
      self.value04:str = obj["value04"]
      self.value05:str = obj["value05"]
      self.value06:str = obj["value06"]
      self.value07:str = obj["value07"]
      self.value08:str = obj["value08"]
      self.value09:str = obj["value09"]
      self.value10:str = obj["value10"]
      self.value11:str = obj["value11"]
      self.value12:str = obj["value12"]
      self.value13:str = obj["value13"]
      self.value14:str = obj["value14"]
      self.value15:str = obj["value15"]
      self.value16:str = obj["value16"]
      self.value17:str = obj["value17"]
      self.value18:str = obj["value18"]
      self.value19:str = obj["value19"]
      self.value20:str = obj["value20"]
      self.value21:str = obj["value21"]
      self.value22:str = obj["value22"]
      self.value23:str = obj["value23"]
      self.value24:str = obj["value24"]
      self.value25:str = obj["value25"]
      self.value26:str = obj["value26"]
      self.value27:str = obj["value27"]
      self.value28:str = obj["value28"]
      self.value29:str = obj["value29"]
      self.value30:str = obj["value30"]
      self.value31:str = obj["value31"]
      self.value32:str = obj["value32"]
      self.value33:str = obj["value33"]
      self.value34:str = obj["value34"]
      self.value35:str = obj["value35"]
      self.value36:str = obj["value36"]
      self.value37:str = obj["value37"]
      self.value38:str = obj["value38"]
      self.value39:str = obj["value39"]
      self.value40:str = obj["value40"]
      self.value41:str = obj["value41"]
      self.value42:str = obj["value42"]
      self.value43:str = obj["value43"]
      self.value44:str = obj["value44"]
      self.value45:str = obj["value45"]
      self.value46:str = obj["value46"]
      self.value47:str = obj["value47"]
      self.value48:str = obj["value48"]
      self.value49:str = obj["value49"]
      self.value50:str = obj["value50"]
      self.value51:str = obj["value51"]
      self.value52:str = obj["value52"]
      self.value53:str = obj["value53"]
      self.value54:str = obj["value54"]
      self.value55:str = obj["value55"]
      self.value56:str = obj["value56"]
      self.value57:str = obj["value57"]
      self.value58:str = obj["value58"]
      self.value59:str = obj["value59"]
      self.value60:str = obj["value60"]
      self.value61:str = obj["value61"]
      self.value62:str = obj["value62"]
      self.value63:str = obj["value63"]
      self.value64:str = obj["value64"]
      self.value65:str = obj["value65"]
      self.value66:str = obj["value66"]
      self.value67:str = obj["value67"]
      self.value68:str = obj["value68"]
      self.value69:str = obj["value69"]
      self.value70:str = obj["value70"]
      self.value71:str = obj["value71"]
      self.value72:str = obj["value72"]
      self.value73:str = obj["value73"]
      self.value74:str = obj["value74"]
      self.value75:str = obj["value75"]
      self.value76:str = obj["value76"]
      self.value77:str = obj["value77"]
      self.value78:str = obj["value78"]
      self.value79:str = obj["value79"]
      self.value80:str = obj["value80"]
      self.value81:str = obj["value81"]
      self.value82:str = obj["value82"]
      self.value83:str = obj["value83"]
      self.value84:str = obj["value84"]
      self.value85:str = obj["value85"]
      self.value86:str = obj["value86"]
      self.value87:str = obj["value87"]
      self.value88:str = obj["value88"]
      self.value89:str = obj["value89"]
      self.value90:str = obj["value90"]
      self.value91:str = obj["value91"]
      self.value92:str = obj["value92"]
      self.value93:str = obj["value93"]
      self.value94:str = obj["value94"]
      self.value95:str = obj["value95"]
      self.value96:str = obj["value96"]
      self.value97:str = obj["value97"]
      self.value98:str = obj["value98"]
      self.value99:str = obj["value99"]
      self.seqId:int = obj["seqId"]
      self.tblname:str = obj["tblname"]
      """  name of tab control record is displayed on  """  
      self.UpdXml:str = obj["UpdXml"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_datafixRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Available:bool = obj["Available"]
      self.AvailDesc:str = obj["AvailDesc"]
      self.ExpiresInd:bool = obj["ExpiresInd"]
      self.Generic:bool = obj["Generic"]
      self.NotGeneric:bool = obj["NotGeneric"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_datafixlistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.seqnum:int = obj["seqnum"]
      self.datafixddefid:str = obj["datafixddefid"]
      self.tblname:str = obj["tblname"]
      self.colname:str = obj["colname"]
      self.width:int = obj["width"]
      self.datatype:str = obj["datatype"]
      self.tabseq:int = obj["tabseq"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CancelReport_input:
   """ Required : 
   SysRowId
   DataFixId
   DataFixSPName
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId of Data Fix record  """  
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix ID  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Procedure  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of report records to return  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class CancelReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   company
   localName
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DataFixDDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.seqnum:int = obj["seqnum"]
      self.datafixddefid:str = obj["datafixddefid"]
      self.tblname:str = obj["tblname"]
      self.colname:str = obj["colname"]
      self.width:int = obj["width"]
      self.datatype:str = obj["datatype"]
      self.tabseq:int = obj["tabseq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataFixListTableset:
   def __init__(self, obj):
      self.datafixlist:list[Erp_Tablesets_datafixlistRow] = obj["datafixlist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DataFixParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.Label01:str = obj["Label01"]
      self.Value01:str = obj["Value01"]
      self.BlankOK01:bool = obj["BlankOK01"]
      self.DataType01:str = obj["DataType01"]
      self.ViewType01:str = obj["ViewType01"]
      self.Label02:str = obj["Label02"]
      self.Value02:str = obj["Value02"]
      self.BlankOK02:bool = obj["BlankOK02"]
      self.DataType02:str = obj["DataType02"]
      self.ViewType02:str = obj["ViewType02"]
      self.Label03:str = obj["Label03"]
      self.Value03:str = obj["Value03"]
      self.BlankOK03:bool = obj["BlankOK03"]
      self.DataType03:str = obj["DataType03"]
      self.ViewType03:str = obj["ViewType03"]
      self.Label04:str = obj["Label04"]
      self.Value04:str = obj["Value04"]
      self.BlankOK04:bool = obj["BlankOK04"]
      self.DataType04:str = obj["DataType04"]
      self.ViewType04:str = obj["ViewType04"]
      self.Label05:str = obj["Label05"]
      self.Value05:str = obj["Value05"]
      self.BlankOK05:bool = obj["BlankOK05"]
      self.DataType05:str = obj["DataType05"]
      self.ViewType05:str = obj["ViewType05"]
      self.Label06:str = obj["Label06"]
      self.Value06:str = obj["Value06"]
      self.BlankOK06:bool = obj["BlankOK06"]
      self.DataType06:str = obj["DataType06"]
      self.ViewType06:str = obj["ViewType06"]
      self.Label07:str = obj["Label07"]
      self.Value07:str = obj["Value07"]
      self.BlankOK07:bool = obj["BlankOK07"]
      self.DataType07:str = obj["DataType07"]
      self.ViewType07:str = obj["ViewType07"]
      self.Label08:str = obj["Label08"]
      self.Value08:str = obj["Value08"]
      self.BlankOK08:bool = obj["BlankOK08"]
      self.DataType08:str = obj["DataType08"]
      self.ViewType08:str = obj["ViewType08"]
      self.Label09:str = obj["Label09"]
      self.Value09:str = obj["Value09"]
      self.BlankOK09:bool = obj["BlankOK09"]
      self.DataType09:str = obj["DataType09"]
      self.ViewType09:str = obj["ViewType09"]
      self.Label10:str = obj["Label10"]
      self.Value10:str = obj["Value10"]
      self.BlankOK10:bool = obj["BlankOK10"]
      self.DataType10:str = obj["DataType10"]
      self.ViewType10:str = obj["ViewType10"]
      self.Label11:str = obj["Label11"]
      self.Value11:str = obj["Value11"]
      self.BlankOK11:bool = obj["BlankOK11"]
      self.DataType11:str = obj["DataType11"]
      self.ViewType11:str = obj["ViewType11"]
      self.Label12:str = obj["Label12"]
      self.Value12:str = obj["Value12"]
      self.BlankOK12:bool = obj["BlankOK12"]
      self.DataType12:str = obj["DataType12"]
      self.ViewType12:str = obj["ViewType12"]
      self.Label13:str = obj["Label13"]
      self.Value13:str = obj["Value13"]
      self.BlankOK13:bool = obj["BlankOK13"]
      self.DataType13:str = obj["DataType13"]
      self.ViewType13:str = obj["ViewType13"]
      self.Label14:str = obj["Label14"]
      self.Value14:str = obj["Value14"]
      self.BlankOK14:bool = obj["BlankOK14"]
      self.DataType14:str = obj["DataType14"]
      self.ViewType14:str = obj["ViewType14"]
      self.Label15:str = obj["Label15"]
      self.Value15:str = obj["Value15"]
      self.BlankOK15:bool = obj["BlankOK15"]
      self.DataType15:str = obj["DataType15"]
      self.ViewType15:str = obj["ViewType15"]
      self.Label16:str = obj["Label16"]
      self.Value16:str = obj["Value16"]
      self.BlankOK16:bool = obj["BlankOK16"]
      self.DataType16:str = obj["DataType16"]
      self.ViewType16:str = obj["ViewType16"]
      self.Label17:str = obj["Label17"]
      self.Value17:str = obj["Value17"]
      self.BlankOK17:bool = obj["BlankOK17"]
      self.DataType17:str = obj["DataType17"]
      self.ViewType17:str = obj["ViewType17"]
      self.Label18:str = obj["Label18"]
      self.Value18:str = obj["Value18"]
      self.BlankOK18:bool = obj["BlankOK18"]
      self.DataType18:str = obj["DataType18"]
      self.ViewType18:str = obj["ViewType18"]
      self.Label19:str = obj["Label19"]
      self.Value19:str = obj["Value19"]
      self.BlankOK19:bool = obj["BlankOK19"]
      self.DataType19:str = obj["DataType19"]
      self.ViewType19:str = obj["ViewType19"]
      self.Label20:str = obj["Label20"]
      self.Value20:str = obj["Value20"]
      self.BlankOK20:bool = obj["BlankOK20"]
      self.DataType20:str = obj["DataType20"]
      self.ViewType20:str = obj["ViewType20"]
      self.BlankCompOK:bool = obj["BlankCompOK"]
      self.LabelComp:str = obj["LabelComp"]
      self.ViewTypeComp:str = obj["ViewTypeComp"]
      self.ValueComp:str = obj["ValueComp"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataFixRptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LocalName:str = obj["LocalName"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.UpdInd:bool = obj["UpdInd"]
      self.UpdTable:str = obj["UpdTable"]
      self.value01:str = obj["value01"]
      self.value02:str = obj["value02"]
      self.value03:str = obj["value03"]
      self.value04:str = obj["value04"]
      self.value05:str = obj["value05"]
      self.value06:str = obj["value06"]
      self.value07:str = obj["value07"]
      self.value08:str = obj["value08"]
      self.value09:str = obj["value09"]
      self.value10:str = obj["value10"]
      self.value11:str = obj["value11"]
      self.value12:str = obj["value12"]
      self.value13:str = obj["value13"]
      self.value14:str = obj["value14"]
      self.value15:str = obj["value15"]
      self.value16:str = obj["value16"]
      self.value17:str = obj["value17"]
      self.value18:str = obj["value18"]
      self.value19:str = obj["value19"]
      self.value20:str = obj["value20"]
      self.value21:str = obj["value21"]
      self.value22:str = obj["value22"]
      self.value23:str = obj["value23"]
      self.value24:str = obj["value24"]
      self.value25:str = obj["value25"]
      self.value26:str = obj["value26"]
      self.value27:str = obj["value27"]
      self.value28:str = obj["value28"]
      self.value29:str = obj["value29"]
      self.value30:str = obj["value30"]
      self.value31:str = obj["value31"]
      self.value32:str = obj["value32"]
      self.value33:str = obj["value33"]
      self.value34:str = obj["value34"]
      self.value35:str = obj["value35"]
      self.value36:str = obj["value36"]
      self.value37:str = obj["value37"]
      self.value38:str = obj["value38"]
      self.value39:str = obj["value39"]
      self.value40:str = obj["value40"]
      self.value41:str = obj["value41"]
      self.value42:str = obj["value42"]
      self.value43:str = obj["value43"]
      self.value44:str = obj["value44"]
      self.value45:str = obj["value45"]
      self.value46:str = obj["value46"]
      self.value47:str = obj["value47"]
      self.value48:str = obj["value48"]
      self.value49:str = obj["value49"]
      self.value50:str = obj["value50"]
      self.value51:str = obj["value51"]
      self.value52:str = obj["value52"]
      self.value53:str = obj["value53"]
      self.value54:str = obj["value54"]
      self.value55:str = obj["value55"]
      self.value56:str = obj["value56"]
      self.value57:str = obj["value57"]
      self.value58:str = obj["value58"]
      self.value59:str = obj["value59"]
      self.value60:str = obj["value60"]
      self.value61:str = obj["value61"]
      self.value62:str = obj["value62"]
      self.value63:str = obj["value63"]
      self.value64:str = obj["value64"]
      self.value65:str = obj["value65"]
      self.value66:str = obj["value66"]
      self.value67:str = obj["value67"]
      self.value68:str = obj["value68"]
      self.value69:str = obj["value69"]
      self.value70:str = obj["value70"]
      self.value71:str = obj["value71"]
      self.value72:str = obj["value72"]
      self.value73:str = obj["value73"]
      self.value74:str = obj["value74"]
      self.value75:str = obj["value75"]
      self.value76:str = obj["value76"]
      self.value77:str = obj["value77"]
      self.value78:str = obj["value78"]
      self.value79:str = obj["value79"]
      self.value80:str = obj["value80"]
      self.value81:str = obj["value81"]
      self.value82:str = obj["value82"]
      self.value83:str = obj["value83"]
      self.value84:str = obj["value84"]
      self.value85:str = obj["value85"]
      self.value86:str = obj["value86"]
      self.value87:str = obj["value87"]
      self.value88:str = obj["value88"]
      self.value89:str = obj["value89"]
      self.value90:str = obj["value90"]
      self.value91:str = obj["value91"]
      self.value92:str = obj["value92"]
      self.value93:str = obj["value93"]
      self.value94:str = obj["value94"]
      self.value95:str = obj["value95"]
      self.value96:str = obj["value96"]
      self.value97:str = obj["value97"]
      self.value98:str = obj["value98"]
      self.value99:str = obj["value99"]
      self.seqId:int = obj["seqId"]
      self.tblname:str = obj["tblname"]
      """  name of tab control record is displayed on  """  
      self.UpdXml:str = obj["UpdXml"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DataFixTableset:
   def __init__(self, obj):
      self.datafix:list[Erp_Tablesets_datafixRow] = obj["datafix"]
      self.DataFixDDef:list[Erp_Tablesets_DataFixDDefRow] = obj["DataFixDDef"]
      self.DataFixParam:list[Erp_Tablesets_DataFixParamRow] = obj["DataFixParam"]
      self.DataFixRpt:list[Erp_Tablesets_DataFixRptRow] = obj["DataFixRpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ImportDataFixRow:
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      self.FileName:str = obj["FileName"]
      self.FixDate:str = obj["FixDate"]
      self.Imported:bool = obj["Imported"]
      self.ImportMessage:str = obj["ImportMessage"]
      self.RowNum:int = obj["RowNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.Title:str = obj["Title"]
      self.UpdType:str = obj["UpdType"]
      self.Version:str = obj["Version"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportDataFixTableset:
   def __init__(self, obj):
      self.ImportDataFix:list[Erp_Tablesets_ImportDataFixRow] = obj["ImportDataFix"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDataFixTableset:
   def __init__(self, obj):
      self.datafix:list[Erp_Tablesets_datafixRow] = obj["datafix"]
      self.DataFixDDef:list[Erp_Tablesets_DataFixDDefRow] = obj["DataFixDDef"]
      self.DataFixParam:list[Erp_Tablesets_DataFixParamRow] = obj["DataFixParam"]
      self.DataFixRpt:list[Erp_Tablesets_DataFixRptRow] = obj["DataFixRpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_datafixRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Available:bool = obj["Available"]
      self.AvailDesc:str = obj["AvailDesc"]
      self.ExpiresInd:bool = obj["ExpiresInd"]
      self.Generic:bool = obj["Generic"]
      self.NotGeneric:bool = obj["NotGeneric"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_datafixlistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.seqnum:int = obj["seqnum"]
      self.datafixddefid:str = obj["datafixddefid"]
      self.tblname:str = obj["tblname"]
      self.colname:str = obj["colname"]
      self.width:int = obj["width"]
      self.datatype:str = obj["datatype"]
      self.tabseq:int = obj["tabseq"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GenerateParameterComponents_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class GenerateParameterComponents_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetByIDCustom_input:
   """ Required : 
   dataFixId
   PageSize
   """  
   def __init__(self, obj):
      self.dataFixId:str = obj["dataFixId"]
      """  The Data Fix Id  """  
      self.PageSize:int = obj["PageSize"]
      """  number of report records to return  """  
      pass

class GetByIDCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   localName
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
      pass

class GetCompanies_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.companies:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCurrentInstallationID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrentTenantID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetInstallationID_output:
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
      self.returnObj:list[Erp_Tablesets_DataFixListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewdatafix_input:
   """ Required : 
   ds
   company
   localName
   key1
   key2
   key3
   key4
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.localName:str = obj["localName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      pass

class GetNewdatafix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReportSysRowIDUpdate_input:
   """ Required : 
   DataFixId
   DataFixSPName
   InstallationID
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix ID  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Procedure  """  
      self.InstallationID:str = obj["InstallationID"]
      """  Install Id  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of Records to return  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class GetReportSysRowIDUpdate_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReport_input:
   """ Required : 
   DataFixId
   DataFixSPName
   InstallationID
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix ID  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Procedure  """  
      self.InstallationID:str = obj["InstallationID"]
      """  Install Id  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of Records to return  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class GetReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   dataFixWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.dataFixWhereClause:str = obj["dataFixWhereClause"]
      """  where clause for data fixes  """  
      self.pageSize:int = obj["pageSize"]
      """  pagesize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page size  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsDataFix_input:
   """ Required : 
   dataFixWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.dataFixWhereClause:str = obj["dataFixWhereClause"]
      """  where clause for data fixes  """  
      self.pageSize:int = obj["pageSize"]
      """  pagesize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page size  """  
      pass

class GetRowsDataFix_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausedatafix
   whereClauseDataFixDDef
   whereClauseDataFixParam
   whereClauseDataFixRpt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausedatafix:str = obj["whereClausedatafix"]
      self.whereClauseDataFixDDef:str = obj["whereClauseDataFixDDef"]
      self.whereClauseDataFixParam:str = obj["whereClauseDataFixParam"]
      self.whereClauseDataFixRpt:str = obj["whereClauseDataFixRpt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DataFixTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTenants_input:
   """ Required : 
   Tenants
   InstallIds
   """  
   def __init__(self, obj):
      self.Tenants:str = obj["Tenants"]
      """  Tenant Ids  """  
      self.InstallIds:str = obj["InstallIds"]
      """  Install Ids  """  
      pass

class GetTenants_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.Tenants:str = obj["parameters"]
      self.InstallIds:str = obj["parameters"]
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

class ImportDataFix_input:
   """ Required : 
   DataFixId
   RetMessage
   DataFixData
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix Id  """  
      self.RetMessage:str = obj["RetMessage"]
      """  return message  """  
      self.DataFixData:str = obj["DataFixData"]
      """  data fix data  """  
      pass

class ImportDataFix_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.RetMessage:str = obj["parameters"]
      self.DataFixData:list = obj[any]
      pass

      """  output parameters  """  

class PrereadDataFix_input:
   """ Required : 
   FileName
   FixData
   RetMessage
   ds
   """  
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      self.FixData:str = obj["FixData"]
      self.RetMessage:str = obj["RetMessage"]
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class PrereadDataFix_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.RetMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResetFix_input:
   """ Required : 
   DataFixId
   DataFixSPName
   SysRowId
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix Id  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored proc name  """  
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId  """  
      self.PageSize:int = obj["PageSize"]
      """  number of report records to return  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class ResetFix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RunUpdateNoDisplay_input:
   """ Required : 
   DataFixId
   DataFixSPName
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix Id  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Proc Name  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class RunUpdateNoDisplay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RptCnt:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RunUpdate_input:
   """ Required : 
   DataFixId
   DataFixSPName
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix Id  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Proc Name  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class RunUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RptCnt:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SelectAll_input:
   """ Required : 
   DataFixId
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix Id  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class SelectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartReport_input:
   """ Required : 
   SysRowId
   DataFixId
   DataFixSPName
   InstallationID
   PageSize
   agentID
   ds
   """  
   def __init__(self, obj):
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId of Data Fix record  """  
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix ID  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Procedure  """  
      self.InstallationID:str = obj["InstallationID"]
      """  Install ID  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of Records to return  """  
      self.agentID:str = obj["agentID"]
      """  Task Agent  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class StartReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnQuote_input:
   """ Required : 
   avalue
   """  
   def __init__(self, obj):
      self.avalue:str = obj["avalue"]
      """  string with quotes  """  
      pass

class UnQuote_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class UnSelectAll_input:
   """ Required : 
   DataFixId
   ds
   """  
   def __init__(self, obj):
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix Id  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class UnSelectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDataFixTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDataFixTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateReport_input:
   """ Required : 
   SysRowId
   DataFixId
   DataFixSPName
   PageSize
   ds
   """  
   def __init__(self, obj):
      self.SysRowId:str = obj["SysRowId"]
      """  SysRowId of Data Fix record  """  
      self.DataFixId:str = obj["DataFixId"]
      """  Data Fix ID  """  
      self.DataFixSPName:str = obj["DataFixSPName"]
      """  Data Fix Stored Procedure  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of Records to return  """  
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class UpdateReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DataFixTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadLocalImportFile_input:
   """ Required : 
   importFile
   """  
   def __init__(self, obj):
      self.importFile:str = obj["importFile"]
      pass

class UploadLocalImportFile_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportDataFixTableset] = obj["returnObj"]
      pass

