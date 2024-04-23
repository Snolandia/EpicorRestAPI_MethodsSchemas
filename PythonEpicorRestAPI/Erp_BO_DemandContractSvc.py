import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandContractSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DemandContracts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandContracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandContracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts",headers=creds) as resp:
           return await resp.json()

async def post_DemandContracts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandContracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandContracts_Company_DemandContractNum(Company, DemandContractNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandContract item
   Description: Calls GetByID to retrieve the DemandContract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandContracts_Company_DemandContractNum(Company, DemandContractNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandContract for the service
   Description: Calls UpdateExt to update DemandContract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandContracts_Company_DemandContractNum(Company, DemandContractNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandContract item
   Description: Call UpdateExt to delete DemandContract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandContract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandContracts_Company_DemandContractNum_DmdCntDtls(Company, DemandContractNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DmdCntDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DmdCntDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntDtls",headers=creds) as resp:
           return await resp.json()

async def get_DemandContracts_Company_DemandContractNum_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmdCntDtl item
   Description: Calls GetByID to retrieve the DmdCntDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandContracts_Company_DemandContractNum_DmdCntHdrAttches(Company, DemandContractNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DmdCntHdrAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DmdCntHdrAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntHdrAttches",headers=creds) as resp:
           return await resp.json()

async def get_DemandContracts_Company_DemandContractNum_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company, DemandContractNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmdCntHdrAttch item
   Description: Calls GetByID to retrieve the DmdCntHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntHdrAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DemandContracts(" + Company + "," + DemandContractNum + ")/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DmdCntDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DmdCntDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmdCntDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls",headers=creds) as resp:
           return await resp.json()

async def post_DmdCntDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmdCntDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmdCntDtl item
   Description: Calls GetByID to retrieve the DmdCntDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DmdCntDtl for the service
   Description: Calls UpdateExt to update DmdCntDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmdCntDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DmdCntDtls_Company_DemandContractNum_DemandContractLine(Company, DemandContractNum, DemandContractLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DmdCntDtl item
   Description: Call UpdateExt to delete DmdCntDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmdCntDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_DmdCntDtls_Company_DemandContractNum_DemandContractLine_DmdCntDtlAttches(Company, DemandContractNum, DemandContractLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DmdCntDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DmdCntDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")/DmdCntDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_DmdCntDtls_Company_DemandContractNum_DemandContractLine_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company, DemandContractNum, DemandContractLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmdCntDtlAttch item
   Description: Calls GetByID to retrieve the DmdCntDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtls(" + Company + "," + DemandContractNum + "," + DemandContractLine + ")/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DmdCntDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DmdCntDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmdCntDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_DmdCntDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmdCntDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company, DemandContractNum, DemandContractLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmdCntDtlAttch item
   Description: Calls GetByID to retrieve the DmdCntDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company, DemandContractNum, DemandContractLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DmdCntDtlAttch for the service
   Description: Calls UpdateExt to update DmdCntDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmdCntDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DmdCntDtlAttches_Company_DemandContractNum_DemandContractLine_DrawingSeq(Company, DemandContractNum, DemandContractLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DmdCntDtlAttch item
   Description: Call UpdateExt to delete DmdCntDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmdCntDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandContractLine: Desc: DemandContractLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntDtlAttches(" + Company + "," + DemandContractNum + "," + DemandContractLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DmdCntHdrAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DmdCntHdrAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmdCntHdrAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches",headers=creds) as resp:
           return await resp.json()

async def post_DmdCntHdrAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmdCntHdrAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company, DemandContractNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmdCntHdrAttch item
   Description: Calls GetByID to retrieve the DmdCntHdrAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmdCntHdrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company, DemandContractNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DmdCntHdrAttch for the service
   Description: Calls UpdateExt to update DmdCntHdrAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmdCntHdrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DmdCntHdrAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DmdCntHdrAttches_Company_DemandContractNum_DrawingSeq(Company, DemandContractNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DmdCntHdrAttch item
   Description: Call UpdateExt to delete DmdCntHdrAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmdCntHdrAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/DmdCntHdrAttches(" + Company + "," + DemandContractNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DmdCntHdrListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDmdCntHdr, whereClauseDmdCntHdrAttch, whereClauseDmdCntDtl, whereClauseDmdCntDtlAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDmdCntHdr=" + whereClauseDmdCntHdr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDmdCntHdrAttch=" + whereClauseDmdCntHdrAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDmdCntDtl=" + whereClauseDmdCntDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDmdCntDtlAttch=" + whereClauseDmdCntDtlAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(demandContractNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "demandContractNum=" + demandContractNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrValue
   Description: To change the currency value
   OperationID: ChangeCurrValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLineUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLineUnitPrice
   Description: Called when the contract line unit price is changing
   OperationID: ChangeLineUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLineUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLineUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDCDtlSellingTotalContractQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDCDtlSellingTotalContractQty
   Description: Update DmdCntDtl information when Customer Part Number is changed.
   OperationID: ChangeDCDtlSellingTotalContractQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDCDtlSellingTotalContractQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDCDtlSellingTotalContractQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDCDtlTotalContractQtyUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDCDtlTotalContractQtyUOM
   Description: Update DmdCntDtl Totals UOM when TotalContract Quantity UOM is changed.
   OperationID: ChangeDCDtlTotalContractQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDCDtlTotalContractQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDCDtlTotalContractQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntDtlMktgCamp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntDtlMktgCamp
   Description: Update MktgCampaign on the DmdCntDtl.
   OperationID: ChangeDmdCntDtlMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntDtlMktgEvnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntDtlMktgEvnt
   Description: Update MktgEvnt on the DmdCntDtl.
   OperationID: ChangeDmdCntDtlMktgEvnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlMktgEvnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlMktgEvnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntDtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntDtlPartNum
   Description: Update DmdCntDtl information when Part Number is changed.
   OperationID: ChangeDmdCntDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntDtlProject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntDtlProject
   Description: Update ProjectID on the DmdCntDtl.
   OperationID: ChangeDmdCntDtlProject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlProject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlProject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntDtlPriceTolerance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntDtlPriceTolerance
   OperationID: ChangeDmdCntDtlPriceTolerance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlPriceTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlPriceTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntDtlXPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntDtlXPartNum
   Description: Update DmdCntDtl infomation when Customer Part Number is changed.
   OperationID: ChangeDmdCntDtlXPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntDtlXPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntDtlXPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntHdrBTCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntHdrBTCustNum
   Description: Update DmdCntHdr information when Bill To Customer is changed.
   OperationID: ChangeDmdCntHdrBTCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntHdrBTCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntHdrBTCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntHdrCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntHdrCustID
   Description: Update Order Header information with values from the Sold To when the Sold To is changed.
   OperationID: ChangeDmdCntHdrCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntHdrCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntHdrCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDmdCntHdrProject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDmdCntHdrProject
   Description: Update ProjectID on the DmdCntHdr.
   OperationID: ChangeDmdCntHdrProject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDmdCntHdrProject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDmdCntHdrProject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseDmdCntHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseDmdCntHdr
   Description: Closes the Demand Contract Header.
   OperationID: CloseDmdCntHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseDmdCntHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDmdCntHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByDemandContractCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByDemandContractCustID
   Description: Gets row by DemandContract.
   OperationID: GetByDemandContractCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDemandContractCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDemandContractCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByDmdCntTradingPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByDmdCntTradingPartner
   Description: Gets row by DemandContract.
   OperationID: GetByDmdCntTradingPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDmdCntTradingPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDmdCntTradingPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractNumByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractNumByID
   Description: Gets contract number by contract id.
   OperationID: GetContractNumByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractNumByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractNumByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshPlant
   Description: Update Plant on DemandDetail related records.
   OperationID: RefreshPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByCustNumDemandContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByCustNumDemandContract
   Description: Returns Demand Contract records for a customer and demand contract
   OperationID: GetByCustNumDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByCustNumDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCustNumDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDmdCntHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDmdCntHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDmdCntHdrAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDmdCntHdrAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntHdrAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntHdrAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntHdrAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDmdCntDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDmdCntDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDmdCntDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDmdCntDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmdCntDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmdCntDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmdCntDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandContractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DmdCntDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DmdCntDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DmdCntHdrAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DmdCntHdrListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DmdCntHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DmdCntHdrRow] = obj["value"]
      pass

class Erp_Tablesets_DmdCntDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandContractLine:int = obj["DemandContractLine"]
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

class Erp_Tablesets_DmdCntDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations.  """  
      self.DocPriceTolerance:int = obj["DocPriceTolerance"]
      """  Defines the tolerance for price difference validations in document currency.  """  
      self.Rpt1PriceTolerance:int = obj["Rpt1PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt2PriceTolerance:int = obj["Rpt2PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt3PriceTolerance:int = obj["Rpt3PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.TotOrdShpInvCallOffQtyUOM:str = obj["TotOrdShpInvCallOffQtyUOM"]
      """  Ordered Qty, Shipped Qty, Invoiced Qty, Minimum Call Off UOM  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DmdCntHdrAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
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

class Erp_Tablesets_DmdCntHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the demand contract.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the contract.  """  
      self.FirmDays:int = obj["FirmDays"]
      """  The number of days from today for which a scheduled quantity is considered firm.  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.ContractComments:str = obj["ContractComments"]
      """  Comments about the demand contract.  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  """  
      self.OpenContract:bool = obj["OpenContract"]
      """  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.MatchByRef:bool = obj["MatchByRef"]
      """  When matching, match demands to order releases by reference number.  """  
      self.MatchByReqDate:bool = obj["MatchByReqDate"]
      """  When matching, match demands to order releases by ship by (reqdate) date.  """  
      self.MatchByQty:bool = obj["MatchByQty"]
      """  When matching, match demands to order releases by quantity.  """  
      self.MatchByOpen:bool = obj["MatchByOpen"]
      """  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  """  
      self.MatchSeqRef:int = obj["MatchSeqRef"]
      """  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  """  
      self.MatchSeqReqDate:int = obj["MatchSeqReqDate"]
      """  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  """  
      self.MatchSeqQty:int = obj["MatchSeqQty"]
      """  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  """  
      self.MatchSeqOpen:int = obj["MatchSeqOpen"]
      """  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  """  
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Hold for Review  """  
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      """  Flag to decide if the non matched schedules needs to be closed.  """  
      self.WFLockByLine:bool = obj["WFLockByLine"]
      """  Flag that state if the work flow error will be checked in every line.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  rate group code  """  
      self.PerfectMatch:bool = obj["PerfectMatch"]
      """  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  """  
      self.MatchPriorityList:str = obj["MatchPriorityList"]
      """  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MatchOptionAvailList:str = obj["MatchOptionAvailList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.MatchOptSelectedList:str = obj["MatchOptSelectedList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.Name:str = obj["Name"]
      """  Address Name  """  
      self.ContractAddressList:str = obj["ContractAddressList"]
      """  Customer Address displays on Demand Contract Summary and Header Detail Screen  """  
      self.FAXNum:str = obj["FAXNum"]
      """  FAX Number  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone Number  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      """  Description of the reservation priority. Example "High".  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DmdCntHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  """  
      self.DemandContract1:str = obj["DemandContract1"]
      self.StartDate:str = obj["StartDate"]
      """  The start date of the demand contract.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the contract.  """  
      self.FirmDays:int = obj["FirmDays"]
      """  The number of days from today for which a scheduled quantity is considered firm.  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.ContractComments:str = obj["ContractComments"]
      """  Comments about the demand contract.  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  """  
      self.OpenContract:bool = obj["OpenContract"]
      """  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.MatchByRef:bool = obj["MatchByRef"]
      """  When matching, match demands to order releases by reference number.  """  
      self.MatchByReqDate:bool = obj["MatchByReqDate"]
      """  When matching, match demands to order releases by ship by (reqdate) date.  """  
      self.MatchByQty:bool = obj["MatchByQty"]
      """  When matching, match demands to order releases by quantity.  """  
      self.MatchByOpen:bool = obj["MatchByOpen"]
      """  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  """  
      self.MatchSeqRef:int = obj["MatchSeqRef"]
      """  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  """  
      self.MatchSeqReqDate:int = obj["MatchSeqReqDate"]
      """  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  """  
      self.MatchSeqQty:int = obj["MatchSeqQty"]
      """  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  """  
      self.MatchSeqOpen:int = obj["MatchSeqOpen"]
      """  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  """  
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Hold for Review  """  
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      """  Flag to decide if the non matched schedules needs to be closed.  """  
      self.WFLockByLine:bool = obj["WFLockByLine"]
      """  Flag that state if the work flow error will be checked in every line.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  rate group code  """  
      self.PerfectMatch:bool = obj["PerfectMatch"]
      """  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  """  
      self.MatchPriorityList:str = obj["MatchPriorityList"]
      """  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowNonPerfectMatch:bool = obj["AllowNonPerfectMatch"]
      """  This option should be defaulted to false. If the user manually turns on this flag then the system will match the schedules as it is working today. If that flag is turned off then the system will match the schedules  only and only if all the criterias selected in the matching options matches between the schedules and the releases.  """  
      self.MatchOptionAvailList:str = obj["MatchOptionAvailList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.MatchOptSelectedList:str = obj["MatchOptSelectedList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.ExcludeUntil:bool = obj["ExcludeUntil"]
      """  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is from Today until the resulting date of adding UntilDays to TODAY  """  
      self.ExcludeBefore:bool = obj["ExcludeBefore"]
      """  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is FROM the resulting date of substracting BeforeDays from TODAY and until TODAY  """  
      self.UntilDays:int = obj["UntilDays"]
      """  Number of days that will be added to TODAY when ExcludeUntil is TRUE. The Cancel Non Match logic will then skip any schedule whose NeedByDate is between TODAY and the resulting date (TODAY + UntilDays).  """  
      self.BeforeDays:int = obj["BeforeDays"]
      """  Number of days that will be substracting TODAY, the resulting date will tell the Cancel Non Match to skip any schedule with a NeedByDate within this date and the current date.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.ContractAddressList:str = obj["ContractAddressList"]
      """  Customer Address displays on Demand Contract Summary and Header Detail Screen  """  
      self.FAXNum:str = obj["FAXNum"]
      """  FAX Number  """  
      self.Name:str = obj["Name"]
      """  Address Name  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone Number  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.ContractAddressFormatted:str = obj["ContractAddressFormatted"]
      """  The formatted Contract Address  """  
      self.MatchOptionsList:str = obj["MatchOptionsList"]
      """  List of available match options  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCurrValue_input:
   """ Required : 
   ipReplaceValue
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipReplaceValue:int = obj["ipReplaceValue"]
      """  ReplaceValue that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeCurrValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDCDtlSellingTotalContractQty_input:
   """ Required : 
   iSellingTotalContractQty
   ds
   """  
   def __init__(self, obj):
      self.iSellingTotalContractQty:int = obj["iSellingTotalContractQty"]
      """  The Selling Total Contract Quantity  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDCDtlSellingTotalContractQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDCDtlTotalContractQtyUOM_input:
   """ Required : 
   iTotalContractQtyUOM
   ds
   """  
   def __init__(self, obj):
      self.iTotalContractQtyUOM:str = obj["iTotalContractQtyUOM"]
      """  The Total Contract Quantity  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDCDtlTotalContractQtyUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntDtlMktgCamp_input:
   """ Required : 
   iMktgCampaignID
   ds
   """  
   def __init__(self, obj):
      self.iMktgCampaignID:str = obj["iMktgCampaignID"]
      """  The Marketing Campaign ID  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntDtlMktgCamp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntDtlMktgEvnt_input:
   """ Required : 
   iMktgEvntSeq
   ds
   """  
   def __init__(self, obj):
      self.iMktgEvntSeq:int = obj["iMktgEvntSeq"]
      """  The Marketing Event  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntDtlMktgEvnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntDtlPartNum_input:
   """ Required : 
   ds
   iPartNum
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      self.iPartNum:str = obj["iPartNum"]
      """  The Part Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class ChangeDmdCntDtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      self.iPartNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class ChangeDmdCntDtlPriceTolerance_input:
   """ Required : 
   iPriceTolerance
   ds
   """  
   def __init__(self, obj):
      self.iPriceTolerance:int = obj["iPriceTolerance"]
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntDtlPriceTolerance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntDtlProject_input:
   """ Required : 
   iProjectID
   ds
   """  
   def __init__(self, obj):
      self.iProjectID:str = obj["iProjectID"]
      """  The ProjectID  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntDtlProject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntDtlXPartNum_input:
   """ Required : 
   iPartNum
   iXPartNum
   ds
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  The Customer Part Number  """  
      self.iXPartNum:str = obj["iXPartNum"]
      """  The Customer Part Number  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntDtlXPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntHdrBTCustNum_input:
   """ Required : 
   iBTCustNum
   ds
   """  
   def __init__(self, obj):
      self.iBTCustNum:int = obj["iBTCustNum"]
      """  The Bill To Customer Number  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntHdrBTCustNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntHdrCustID_input:
   """ Required : 
   iCustID
   ds
   """  
   def __init__(self, obj):
      self.iCustID:str = obj["iCustID"]
      """  The Customer Number  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntHdrCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDmdCntHdrProject_input:
   """ Required : 
   iProjectID
   ds
   """  
   def __init__(self, obj):
      self.iProjectID:str = obj["iProjectID"]
      """  The ProjectID  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeDmdCntHdrProject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLineUnitPrice_input:
   """ Required : 
   unitPrice
   baseOrDoc
   unitPriceOverride
   ds
   """  
   def __init__(self, obj):
      self.unitPrice:int = obj["unitPrice"]
      """  The proposed unit price value  """  
      self.baseOrDoc:str = obj["baseOrDoc"]
      """  (B)ase or (D) unit price  """  
      self.unitPriceOverride:bool = obj["unitPriceOverride"]
      """  Indicates the user chooses to override the unit price  """  
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class ChangeLineUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CloseDmdCntHdr_input:
   """ Required : 
   iDemandContractNum
   iOpenContract
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The Demand Contract Number  """  
      self.iOpenContract:bool = obj["iOpenContract"]
      """  The Demand Contract Number  """  
      pass

class CloseDmdCntHdr_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   demandContractNum
   """  
   def __init__(self, obj):
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DemandContractTableset:
   def __init__(self, obj):
      self.DmdCntHdr:list[Erp_Tablesets_DmdCntHdrRow] = obj["DmdCntHdr"]
      self.DmdCntHdrAttch:list[Erp_Tablesets_DmdCntHdrAttchRow] = obj["DmdCntHdrAttch"]
      self.DmdCntDtl:list[Erp_Tablesets_DmdCntDtlRow] = obj["DmdCntDtl"]
      self.DmdCntDtlAttch:list[Erp_Tablesets_DmdCntDtlAttchRow] = obj["DmdCntDtlAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DmdCntDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandContractLine:int = obj["DemandContractLine"]
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

class Erp_Tablesets_DmdCntDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  Is the link to the DemandContractHdr table.  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandContractDtl record for the contract and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.
A default should be made when the DemandContractDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  Determines whether or not this contract line is being run in a test mode. When contracts are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.SellingTotalContractQty:int = obj["SellingTotalContractQty"]
      """  The total selling quantity expected to be ordered for this line over the life of the contract.  """  
      self.TotalContractQty:int = obj["TotalContractQty"]
      """  The total quantity expected to be ordered for this line over the life of the contract.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the Customer.DiscountPercent.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractDtl record. Can be blank.  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the order line with.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.DetailComments:str = obj["DetailComments"]
      """  Comments about the demand detail line.  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  Use standard Epicor Price matrix/logic  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders lines invoiced for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract line in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderedQty:int = obj["TotalOrderedQty"]
      """  The total actual quantity ordered for this contract line. (credit memos may change it to negative).  """  
      self.TotalShippedQty:int = obj["TotalShippedQty"]
      """  The total actual quantity shipped for this contract line. (credit memos may change it to negative).  """  
      self.TotalInvoicedQty:int = obj["TotalInvoicedQty"]
      """  The total actual quantity invoiced for this contract line. (credit memos may change it to negative).  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  Indicates if current open Order Releases that have not been shipped and do not have a job should be deleted when processing the demand.  Provides the default value for DemandDetail.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via Demand Contract entry if the CRM module is installed.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via demand contract entry if the CRM module is installed.  """  
      self.MinCallOffQty:int = obj["MinCallOffQty"]
      """  The mininum quantity that should be for each individual demand schedule record. If the schedule quantity is less than the minimum call off quantity, a warning will be issued but processing can continue.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the  part revision.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  """  
      self.DemandPricing:str = obj["DemandPricing"]
      """  Defines if Internal Pricing or Customer Pricing will be used for checking price differences  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Same as Unit price except that this field contains the unit price in a report currency  """  
      self.OTSmartString:bool = obj["OTSmartString"]
      """  When set to TRUE the smart string functionality will only be processed when the incoming demand is new. After it has been processed and saved, if a retransmission is sent the smart string values will be ignored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations.  """  
      self.DocPriceTolerance:int = obj["DocPriceTolerance"]
      """  Defines the tolerance for price difference validations in document currency.  """  
      self.Rpt1PriceTolerance:int = obj["Rpt1PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt2PriceTolerance:int = obj["Rpt2PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.Rpt3PriceTolerance:int = obj["Rpt3PriceTolerance"]
      """  Defines the tolerance for price difference validations in a report currency.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.SelectedForDemand:bool = obj["SelectedForDemand"]
      """  Indicates if this record has been selected to create a demand detail record.  Used for automatically creating DemandDetail records from contract lines.  """  
      self.TotOrdShpInvCallOffQtyUOM:str = obj["TotOrdShpInvCallOffQtyUOM"]
      """  Ordered Qty, Shipped Qty, Invoiced Qty, Minimum Call Off UOM  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BitFlag:int = obj["BitFlag"]
      self.DemandCntHdrDemandContract:str = obj["DemandCntHdrDemandContract"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DmdCntHdrAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DemandContractNum:int = obj["DemandContractNum"]
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

class Erp_Tablesets_DmdCntHdrListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the demand contract.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the contract.  """  
      self.FirmDays:int = obj["FirmDays"]
      """  The number of days from today for which a scheduled quantity is considered firm.  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.ContractComments:str = obj["ContractComments"]
      """  Comments about the demand contract.  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  """  
      self.OpenContract:bool = obj["OpenContract"]
      """  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.MatchByRef:bool = obj["MatchByRef"]
      """  When matching, match demands to order releases by reference number.  """  
      self.MatchByReqDate:bool = obj["MatchByReqDate"]
      """  When matching, match demands to order releases by ship by (reqdate) date.  """  
      self.MatchByQty:bool = obj["MatchByQty"]
      """  When matching, match demands to order releases by quantity.  """  
      self.MatchByOpen:bool = obj["MatchByOpen"]
      """  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  """  
      self.MatchSeqRef:int = obj["MatchSeqRef"]
      """  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  """  
      self.MatchSeqReqDate:int = obj["MatchSeqReqDate"]
      """  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  """  
      self.MatchSeqQty:int = obj["MatchSeqQty"]
      """  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  """  
      self.MatchSeqOpen:int = obj["MatchSeqOpen"]
      """  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  """  
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Hold for Review  """  
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      """  Flag to decide if the non matched schedules needs to be closed.  """  
      self.WFLockByLine:bool = obj["WFLockByLine"]
      """  Flag that state if the work flow error will be checked in every line.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  rate group code  """  
      self.PerfectMatch:bool = obj["PerfectMatch"]
      """  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  """  
      self.MatchPriorityList:str = obj["MatchPriorityList"]
      """  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MatchOptionAvailList:str = obj["MatchOptionAvailList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.MatchOptSelectedList:str = obj["MatchOptSelectedList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.Name:str = obj["Name"]
      """  Address Name  """  
      self.ContractAddressList:str = obj["ContractAddressList"]
      """  Customer Address displays on Demand Contract Summary and Header Detail Screen  """  
      self.FAXNum:str = obj["FAXNum"]
      """  FAX Number  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone Number  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      """  Description of the reservation priority. Example "High".  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DmdCntHdrListTableset:
   def __init__(self, obj):
      self.DmdCntHdrList:list[Erp_Tablesets_DmdCntHdrListRow] = obj["DmdCntHdrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DmdCntHdrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  System assigned internal number to uniquely identify the demand contract record.  The number comes from Sequence DemandContractNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the demand contract is for.  This must be valid in the Customer table.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the demand contract.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the contract.  """  
      self.FirmDays:int = obj["FirmDays"]
      """  The number of days from today for which a scheduled quantity is considered firm.  """  
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      """  The trading partner name.  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  Values are:  PART - By Part  PO - By Part/PO  """  
      self.FOB:str = obj["FOB"]
      """  An optional field that describes the FOB policy.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of DemandContractHdr.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  """  
      self.ContractComments:str = obj["ContractComments"]
      """  Comments about the demand contract.  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record for this DemandContractHdr record. Can be blank.  """  
      self.OpenContract:bool = obj["OpenContract"]
      """  Indicates if this contract is in an "open" status.  When a contract is closed, all DemandHead records that are associated with the contract will also be set to closed.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  The user that entered the contract.  On new demand contracts use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.TotalInvoiceAmt:int = obj["TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.TotalOrderAmt:int = obj["TotalOrderAmt"]
      """  Total  amount of orders for this contract in base currency. This field has a true sign. (credit memos are negative).  """  
      self.MatchByRef:bool = obj["MatchByRef"]
      """  When matching, match demands to order releases by reference number.  """  
      self.MatchByReqDate:bool = obj["MatchByReqDate"]
      """  When matching, match demands to order releases by ship by (reqdate) date.  """  
      self.MatchByQty:bool = obj["MatchByQty"]
      """  When matching, match demands to order releases by quantity.  """  
      self.MatchByOpen:bool = obj["MatchByOpen"]
      """  When matching, match demands to order releases by matching the first open demand and the first open release.  All subsequent open demands and releases not already matched will be matched.  Subsequent demands and releases are determined by querying the tables by reqdate.  """  
      self.MatchSeqRef:int = obj["MatchSeqRef"]
      """  Indicates where reference matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByRef is false.  """  
      self.MatchSeqReqDate:int = obj["MatchSeqReqDate"]
      """  Indicates where date matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByReqDate is false.  """  
      self.MatchSeqQty:int = obj["MatchSeqQty"]
      """  Indicates where quantity matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByQty is false.  """  
      self.MatchSeqOpen:int = obj["MatchSeqOpen"]
      """  Indicates where open matching falls in the matching heirarchy of the MatchBy options selected.  Valid values are 1-4, may be zero when MatchByOpen is false.  """  
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      """  Hold for Review  """  
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      """  Flag to decide if the non matched schedules needs to be closed.  """  
      self.WFLockByLine:bool = obj["WFLockByLine"]
      """  Flag that state if the work flow error will be checked in every line.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  rate group code  """  
      self.PerfectMatch:bool = obj["PerfectMatch"]
      """  When true this field will indicate that Demand Schedules and Releases will only be matched if they meet all priorities listed in the Matching Priority List.  """  
      self.MatchPriorityList:str = obj["MatchPriorityList"]
      """  A list of priorities in which the matching will be executed, first items are of higher priority than items at the last of the list.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowNonPerfectMatch:bool = obj["AllowNonPerfectMatch"]
      """  This option should be defaulted to false. If the user manually turns on this flag then the system will match the schedules as it is working today. If that flag is turned off then the system will match the schedules  only and only if all the criterias selected in the matching options matches between the schedules and the releases.  """  
      self.MatchOptionAvailList:str = obj["MatchOptionAvailList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.MatchOptSelectedList:str = obj["MatchOptSelectedList"]
      """  A LIST-DELIM delimited list of part options  """  
      self.ExcludeUntil:bool = obj["ExcludeUntil"]
      """  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is from Today until the resulting date of adding UntilDays to TODAY  """  
      self.ExcludeBefore:bool = obj["ExcludeBefore"]
      """  When TRUE, the Cancel Non Matched logic will skip any schedule whose NeedByDate is FROM the resulting date of substracting BeforeDays from TODAY and until TODAY  """  
      self.UntilDays:int = obj["UntilDays"]
      """  Number of days that will be added to TODAY when ExcludeUntil is TRUE. The Cancel Non Match logic will then skip any schedule whose NeedByDate is between TODAY and the resulting date (TODAY + UntilDays).  """  
      self.BeforeDays:int = obj["BeforeDays"]
      """  Number of days that will be substracting TODAY, the resulting date will tell the Cancel Non Match to skip any schedule with a NeedByDate within this date and the current date.  """  
      self.DocTotalInvoiceAmt:int = obj["DocTotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalInvoiceAmt:int = obj["Rpt1TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalInvoiceAmt:int = obj["Rpt2TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalInvoiceAmt:int = obj["Rpt3TotalInvoiceAmt"]
      """  Total invoice amount of orders invoiced for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.DocTotalOrderAmt:int = obj["DocTotalOrderAmt"]
      """  Total amount of orders for this contract in document currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt1TotalOrderAmt:int = obj["Rpt1TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt2TotalOrderAmt:int = obj["Rpt2TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.Rpt3TotalOrderAmt:int = obj["Rpt3TotalOrderAmt"]
      """  Total amount of orders for this contract in a report currency. This field has a true sign. (credit memos are negative).  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BillToCustomerName:str = obj["BillToCustomerName"]
      self.ContractAddressList:str = obj["ContractAddressList"]
      """  Customer Address displays on Demand Contract Summary and Header Detail Screen  """  
      self.FAXNum:str = obj["FAXNum"]
      """  FAX Number  """  
      self.Name:str = obj["Name"]
      """  Address Name  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone Number  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.ContractAddressFormatted:str = obj["ContractAddressFormatted"]
      """  The formatted Contract Address  """  
      self.MatchOptionsList:str = obj["MatchOptionsList"]
      """  List of available match options  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDemandContractTableset:
   def __init__(self, obj):
      self.DmdCntHdr:list[Erp_Tablesets_DmdCntHdrRow] = obj["DmdCntHdr"]
      self.DmdCntHdrAttch:list[Erp_Tablesets_DmdCntHdrAttchRow] = obj["DmdCntHdrAttch"]
      self.DmdCntDtl:list[Erp_Tablesets_DmdCntDtlRow] = obj["DmdCntDtl"]
      self.DmdCntDtlAttch:list[Erp_Tablesets_DmdCntDtlAttchRow] = obj["DmdCntDtlAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByCustNumDemandContract_input:
   """ Required : 
   custNum
   demandContract
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer Number  """  
      self.demandContract:str = obj["demandContract"]
      """  Demand Contract  """  
      pass

class GetByCustNumDemandContract_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
      pass

class GetByDemandContractCustID_input:
   """ Required : 
   demandContract
   customerID
   """  
   def __init__(self, obj):
      self.demandContract:str = obj["demandContract"]
      """  DemandContract  """  
      self.customerID:str = obj["customerID"]
      """  Customer ID  """  
      pass

class GetByDemandContractCustID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
      pass

class GetByDmdCntTradingPartner_input:
   """ Required : 
   demandContract
   tradingPartnerName
   """  
   def __init__(self, obj):
      self.demandContract:str = obj["demandContract"]
      """  DemandContract  """  
      self.tradingPartnerName:str = obj["tradingPartnerName"]
      """  Trading Parner Name  """  
      pass

class GetByDmdCntTradingPartner_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   demandContractNum
   """  
   def __init__(self, obj):
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
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

class GetContractNumByID_input:
   """ Required : 
   contractID
   """  
   def __init__(self, obj):
      self.contractID:str = obj["contractID"]
      """  Demand Contract ID  """  
      pass

class GetContractNumByID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.contractNum:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_DmdCntHdrListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDmdCntDtlAttch_input:
   """ Required : 
   ds
   demandContractNum
   demandContractLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandContractLine:int = obj["demandContractLine"]
      pass

class GetNewDmdCntDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDmdCntDtl_input:
   """ Required : 
   ds
   demandContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class GetNewDmdCntDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDmdCntHdrAttch_input:
   """ Required : 
   ds
   demandContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class GetNewDmdCntHdrAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDmdCntHdr_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class GetNewDmdCntHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDmdCntHdr
   whereClauseDmdCntHdrAttch
   whereClauseDmdCntDtl
   whereClauseDmdCntDtlAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDmdCntHdr:str = obj["whereClauseDmdCntHdr"]
      self.whereClauseDmdCntHdrAttch:str = obj["whereClauseDmdCntHdrAttch"]
      self.whereClauseDmdCntDtl:str = obj["whereClauseDmdCntDtl"]
      self.whereClauseDmdCntDtlAttch:str = obj["whereClauseDmdCntDtlAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandContractTableset] = obj["returnObj"]
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

class RefreshPlant_input:
   """ Required : 
   inputDMCNum
   inputDMCLine
   inputDMCPlant
   """  
   def __init__(self, obj):
      self.inputDMCNum:int = obj["inputDMCNum"]
      """  The Demand Contract Num  """  
      self.inputDMCLine:int = obj["inputDMCLine"]
      """  The Demand Contract Line  """  
      self.inputDMCPlant:str = obj["inputDMCPlant"]
      """  The Demand Plant  """  
      pass

class RefreshPlant_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandContractTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandContractTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandContractTableset] = obj["ds"]
      pass

      """  output parameters  """  

