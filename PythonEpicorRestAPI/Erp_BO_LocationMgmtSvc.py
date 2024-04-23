import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LocationMgmtSvc
# Description: class LocationMgmtSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LocationMgmts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationMgmts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts",headers=creds) as resp:
           return await resp.json()

async def post_LocationMgmts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationMgmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationInventoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LocationInventoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum(Company, LocationNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationMgmt item
   Description: Calls GetByID to retrieve the LocationMgmt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationMgmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationInventoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LocationMgmts_Company_LocationNum(Company, LocationNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LocationMgmt for the service
   Description: Calls UpdateExt to update LocationMgmt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationMgmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationInventoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LocationMgmts_Company_LocationNum(Company, LocationNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LocationMgmt item
   Description: Call UpdateExt to delete LocationMgmt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationMgmt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationInventoryAddresses(Company, LocationNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LocationInventoryAddresses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationInventoryAddresses1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryAddressRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationInventoryAddresses",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationInventoryAddresses_Company_LocationNum_AddressType(Company, LocationNum, AddressType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationInventoryAddress item
   Description: Calls GetByID to retrieve the LocationInventoryAddress item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationInventoryAddress1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param AddressType: Desc: AddressType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationMtls(Company, LocationNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LocationMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationMtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationMtls",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company, LocationNum, JobNum, AssemblySeq, MtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationMtl item
   Description: Calls GetByID to retrieve the LocationMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationMtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationTrans(Company, LocationNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LocationTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationTrans",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationTrans_Company_LocationNum_LocationSeqNum(Company, LocationNum, LocationSeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationTran item
   Description: Calls GetByID to retrieve the LocationTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param LocationSeqNum: Desc: LocationSeqNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationWarrantyTrans(Company, LocationNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LocationWarrantyTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LocationWarrantyTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationWarrantyTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationWarrantyTrans",headers=creds) as resp:
           return await resp.json()

async def get_LocationMgmts_Company_LocationNum_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company, LocationNum, WarrantySeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationWarrantyTran item
   Description: Calls GetByID to retrieve the LocationWarrantyTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationWarrantyTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param WarrantySeqNum: Desc: WarrantySeqNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMgmts(" + Company + "," + LocationNum + ")/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationInventoryAddresses(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LocationInventoryAddresses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationInventoryAddresses
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryAddressRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses",headers=creds) as resp:
           return await resp.json()

async def post_LocationInventoryAddresses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationInventoryAddresses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LocationInventoryAddresses_Company_LocationNum_AddressType(Company, LocationNum, AddressType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationInventoryAddress item
   Description: Calls GetByID to retrieve the LocationInventoryAddress item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationInventoryAddress
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param AddressType: Desc: AddressType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LocationInventoryAddresses_Company_LocationNum_AddressType(Company, LocationNum, AddressType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LocationInventoryAddress for the service
   Description: Calls UpdateExt to update LocationInventoryAddress. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationInventoryAddress
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param AddressType: Desc: AddressType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationInventoryAddressRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LocationInventoryAddresses_Company_LocationNum_AddressType(Company, LocationNum, AddressType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LocationInventoryAddress item
   Description: Call UpdateExt to delete LocationInventoryAddress item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationInventoryAddress
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param AddressType: Desc: AddressType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationInventoryAddresses(" + Company + "," + LocationNum + "," + AddressType + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationMtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LocationMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationMtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls",headers=creds) as resp:
           return await resp.json()

async def post_LocationMtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationMtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company, LocationNum, JobNum, AssemblySeq, MtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationMtl item
   Description: Calls GetByID to retrieve the LocationMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company, LocationNum, JobNum, AssemblySeq, MtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LocationMtl for the service
   Description: Calls UpdateExt to update LocationMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LocationMtls_Company_LocationNum_JobNum_AssemblySeq_MtlSeq(Company, LocationNum, JobNum, AssemblySeq, MtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LocationMtl item
   Description: Call UpdateExt to delete LocationMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationMtls(" + Company + "," + LocationNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LocationTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans",headers=creds) as resp:
           return await resp.json()

async def post_LocationTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LocationTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LocationTrans_Company_LocationNum_LocationSeqNum(Company, LocationNum, LocationSeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationTran item
   Description: Calls GetByID to retrieve the LocationTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param LocationSeqNum: Desc: LocationSeqNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LocationTrans_Company_LocationNum_LocationSeqNum(Company, LocationNum, LocationSeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LocationTran for the service
   Description: Calls UpdateExt to update LocationTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param LocationSeqNum: Desc: LocationSeqNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LocationTrans_Company_LocationNum_LocationSeqNum(Company, LocationNum, LocationSeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LocationTran item
   Description: Call UpdateExt to delete LocationTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param LocationSeqNum: Desc: LocationSeqNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationTrans(" + Company + "," + LocationNum + "," + LocationSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LocationWarrantyTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LocationWarrantyTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LocationWarrantyTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationWarrantyTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans",headers=creds) as resp:
           return await resp.json()

async def post_LocationWarrantyTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LocationWarrantyTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company, LocationNum, WarrantySeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LocationWarrantyTran item
   Description: Calls GetByID to retrieve the LocationWarrantyTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LocationWarrantyTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param WarrantySeqNum: Desc: WarrantySeqNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company, LocationNum, WarrantySeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LocationWarrantyTran for the service
   Description: Calls UpdateExt to update LocationWarrantyTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LocationWarrantyTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param WarrantySeqNum: Desc: WarrantySeqNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LocationWarrantyTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LocationWarrantyTrans_Company_LocationNum_WarrantySeqNum(Company, LocationNum, WarrantySeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LocationWarrantyTran item
   Description: Call UpdateExt to delete LocationWarrantyTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LocationWarrantyTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocationNum: Desc: LocationNum   Required: True   Allow empty value : True
      :param WarrantySeqNum: Desc: WarrantySeqNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/LocationWarrantyTrans(" + Company + "," + LocationNum + "," + WarrantySeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LocationInventoryListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLocationInventory, whereClauseLocationInventoryAddress, whereClauseLocationMtl, whereClauseLocationTran, whereClauseLocationWarrantyTran, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseLocationInventory=" + whereClauseLocationInventory
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLocationInventoryAddress=" + whereClauseLocationInventoryAddress
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLocationMtl=" + whereClauseLocationMtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLocationTran=" + whereClauseLocationTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLocationWarrantyTran=" + whereClauseLocationWarrantyTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(locationNum, epicorHeaders = None):
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
   params += "locationNum=" + locationNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangedLocationWarrantyTranPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedLocationWarrantyTranPartNum
   Description: Called when the Part is changed
   OperationID: ChangedLocationWarrantyTranPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedLocationWarrantyTranPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedLocationWarrantyTranPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentAddress
   Description: Returns the address of the requested type: L=Location, O=Owner, S=Sold To
   OperationID: GetCurrentAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustomerAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustomerAddress
   Description: Update Order Header information with values from the Sold To when the Sold To is changed.
   OperationID: GetNewCustomerAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustomerAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustomerAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOTMFAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOTMFAddress
   Description: Update Order Header information with values from the Sold To when the Sold To is changed.
   OperationID: GetNewOTMFAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOTMFAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOTMFAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLocationWarrantyTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLocationWarrantyTran
   Description: Get Location Warranty Transaction
   OperationID: GetLocationWarrantyTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLocationWarrantyTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLocationWarrantyTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedPartNum
   OperationID: ChangedPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedWarrantyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedWarrantyCode
   OperationID: ChangedWarrantyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedWarrantyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedWarrantyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCustomer
   OperationID: ValidateCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShipTo
   OperationID: ValidateShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartNum
   OperationID: ValidatePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSerialNumber
   OperationID: ValidateSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMaterialOrigSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMaterialOrigSerialNumber
   OperationID: ValidateMaterialOrigSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMaterialOrigSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMaterialOrigSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMaterialLotNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMaterialLotNumber
   Description: This method validates Lot number that user can enter in case if multiple lots came up in Original Part search
   OperationID: ValidateMaterialLotNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMaterialLotNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMaterialLotNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateIDNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateIDNumber
   OperationID: ValidateIDNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateIDNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateIDNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLocationInventory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLocationInventory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationInventory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLocationInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLocationInventoryAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLocationInventoryAddress
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationInventoryAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLocationInventoryAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationInventoryAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLocationMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLocationMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLocationMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLocationTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLocationTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLocationTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLocationWarrantyTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLocationWarrantyTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLocationWarrantyTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLocationWarrantyTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLocationWarrantyTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LocationMgmtSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryAddressRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LocationInventoryAddressRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LocationInventoryListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationInventoryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LocationInventoryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationMtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LocationMtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LocationTranRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LocationWarrantyTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LocationWarrantyTranRow] = obj["value"]
      pass

class Erp_Tablesets_LocationInventoryAddressRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID of parent location  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  """  
      self.CustNum:int = obj["CustNum"]
      """  Unique customer number for this location.  """  
      self.CustShipToNum:str = obj["CustShipToNum"]
      """  Ship To number for this locatoin  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the address for this location.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the address for this location.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the address for this location.  """  
      self.City:str = obj["City"]
      """  City portion of the address for this location  """  
      self.Contact:str = obj["Contact"]
      """  Contact for this location.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country Number for this location.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  The email address for this location.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax number for this location  """  
      self.Name:str = obj["Name"]
      """  Name for this location.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone number for this location.  """  
      self.State:str = obj["State"]
      """  State for this location.  """  
      self.Zip:str = obj["Zip"]
      """  Zip for this locatoin  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Use OTS  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ConNum:int = obj["ConNum"]
      """  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  """  
      self.TranComment:str = obj["TranComment"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.CustomerECCType:str = obj["CustomerECCType"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventoryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID for Location Inventory record  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of part.  """  
      self.IDNum:str = obj["IDNum"]
      """  Identification Number (example HIN, VIN).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID for Location Inventory record  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  M  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped.  """  
      self.CurrentOwner:str = obj["CurrentOwner"]
      """  This is the current owner.  Valid values are (D)istributor, (C)ustomer  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Order Comment  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.Listing:str = obj["Listing"]
      """  The type of listing the location inventory item is: L=Leaser, S=Sale  """  
      self.ListingStartDate:str = obj["ListingStartDate"]
      """  Date when the location inventory was listed.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty Comment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  Date the warrany started.  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Date the warranty will expired.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Num  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of part.  """  
      self.IDNum:str = obj["IDNum"]
      """  Identification Number (example HIN, VIN).  """  
      self.WarrantyTransfer:str = obj["WarrantyTransfer"]
      """  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AddrList:str = obj["AddrList"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.ExtAddress1:str = obj["ExtAddress1"]
      self.ExtAddress2:str = obj["ExtAddress2"]
      self.ExtAddress3:str = obj["ExtAddress3"]
      self.ExtCity:str = obj["ExtCity"]
      self.ExtContact:str = obj["ExtContact"]
      self.ExtCountryNum:int = obj["ExtCountryNum"]
      self.ExtEmailAddress:str = obj["ExtEmailAddress"]
      self.ExtFaxNum:str = obj["ExtFaxNum"]
      self.ExtName:str = obj["ExtName"]
      self.ExtPhoneNum:str = obj["ExtPhoneNum"]
      self.ExtState:str = obj["ExtState"]
      self.ExtZIP:str = obj["ExtZIP"]
      self.NewAddrList:str = obj["NewAddrList"]
      self.NewCustID:str = obj["NewCustID"]
      self.NewCustNum:int = obj["NewCustNum"]
      self.NewShipToNum:str = obj["NewShipToNum"]
      self.NewUseOTMF:bool = obj["NewUseOTMF"]
      self.TrackIDNum:bool = obj["TrackIDNum"]
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      self.TranComment:str = obj["TranComment"]
      """  Transaction Comment  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Use OTS  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      """  Sold to address  """  
      self.OwnerAddrList:str = obj["OwnerAddrList"]
      """  Owner address.  """  
      self.LocationAddrList:str = obj["LocationAddrList"]
      """  Location Address.  """  
      self.TransferAddrType:str = obj["TransferAddrType"]
      """  Where is the transfer going to: (N)o Address Change,  (L)ocation, (O)wner, (B)oth.  Blank will be for a warranty change only.  """  
      self.OwnerBusinessModel:str = obj["OwnerBusinessModel"]
      """  Owner Busines Model  """  
      self.LocationBusinessModel:str = obj["LocationBusinessModel"]
      """  Location Business Model  """  
      self.OwnerCustID:str = obj["OwnerCustID"]
      """  Owner Customer ID  """  
      self.OwnerShipToNum:str = obj["OwnerShipToNum"]
      """  Owner Ship To.  """  
      self.OwnerUseOTMF:bool = obj["OwnerUseOTMF"]
      """  Owner Use One Time Mark For.  """  
      self.LocationCustID:str = obj["LocationCustID"]
      """  Location Customer ID.  """  
      self.LocationShipToNum:str = obj["LocationShipToNum"]
      """  Location Ship To.  """  
      self.LocationUseOTMF:bool = obj["LocationUseOTMF"]
      """  Location Use One Time Mark For.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  Sold To Customer ID.  """  
      self.SoldToShipToNum:str = obj["SoldToShipToNum"]
      """  Sold To Ship To.  """  
      self.SoldToUseOTMF:bool = obj["SoldToUseOTMF"]
      """  Sold To Use Ont Time Mark For.  """  
      self.SoldToBusinessModel:str = obj["SoldToBusinessModel"]
      """  Sold To Business Model  """  
      self.OwnerAddrType:str = obj["OwnerAddrType"]
      """  Addres type of owner : L=Locatoin, O=Owner, S=Sold To  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date when transfer occured - writes to LocationTran.EffectiveDate  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      self.NewConNum:int = obj["NewConNum"]
      """  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  """  
      self.LocationAttn:str = obj["LocationAttn"]
      """  External field to hold the name of the selected customer contact for the Location record  """  
      self.NewConName:str = obj["NewConName"]
      """  External field to hold the name of the selected customer contact for the selected record  """  
      self.OwnerAttn:str = obj["OwnerAttn"]
      """  External field to hold the name of the selected customer contact for the Owner record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  """  
      self.Description:str = obj["Description"]
      """  A description of the material.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent.  Field Service was EstQty in FSCallMt.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  The unit used to measure the material.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.  When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """  A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.  It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material.  Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Job Material.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      """  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  """  
      self.SalvageCredit:int = obj["SalvageCredit"]
      """  Total salvage credit to date.  A summary of salvage receipt transactions.  """  
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      """  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  """  
      self.Ordered:bool = obj["Ordered"]
      """  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  """  
      self.PurComment:str = obj["PurComment"]
      """  Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  Indicates if this material will be backflushed.  Note: this field is defaulted from Part.BackFlush Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobMtl is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      """  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      """  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      """  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      """  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """  Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler: 'I' to ignore in eScheduler.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this Material belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this material relates to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the Material in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the Material in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the material in customers currency.  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.Billable:bool = obj["Billable"]
      """  Is this a billable material item.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Holds the quantity of the item that has been shipped through misc.  shipments  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the Material in Customer currency.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  """  
      self.AddedMtl:bool = obj["AddedMtl"]
      """  This material was added after initial setup of the job  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.SCMiscCode:str = obj["SCMiscCode"]
      """  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """  RFQ SRFQ Status: W= Waiting, A = Accepted, R = Requested, C = Receivedtatus.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.WIReqDate:str = obj["WIReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      """  Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """  Unit of Measure of the JobMtl.BaseRequiredQty.  If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  """  
      self.PickError:str = obj["PickError"]
      """  A non blank character indicates that the release could not be picked by the Auto Pick process. The possible values are: "L" - Order Line can't be shipped complete. "O" - Order can't be shipped complete. "I" - Insufficient quantity reserved"Z" - Zero quantity reserved.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """  Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """  Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """  Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      """  Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      """  Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      """  Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      """  Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.LoanedQty:int = obj["LoanedQty"]
      """  The material quantity that has been loaned out to another job.  """  
      self.BorrowedQty:int = obj["BorrowedQty"]
      """  The material quantity that has been borrowed from another job.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      """  IsPOCostingMaintained  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.POCostingFactor:int = obj["POCostingFactor"]
      """  POCostingFactor  """  
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      """  PlannedQtyPerUnit  """  
      self.POCostingDirection:int = obj["POCostingDirection"]
      """  POCostingDirection  """  
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      """  POCostingUnitVal  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.ContractID:str = obj["ContractID"]
      """  Contract ID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.StagingLotNum:str = obj["StagingLotNum"]
      """  Stores the lot number of the material in the Staging Warehouse/Bin.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum  """  
      self.SerialNum:str = obj["SerialNum"]
      """  SerialNum  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  WarrantyCode  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  WarrantyComment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  WarrantyStartDate  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  WarrantyExpirationDate  """  
      self.LocationNum:int = obj["LocationNum"]
      """  LocationNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DealerWarranty:str = obj["DealerWarranty"]
      """  Dealer specific warranty code.  This is a non ERP warranty code.  """  
      self.DealerWarrantyDesc:str = obj["DealerWarrantyDesc"]
      """  Dealer specific warranty description  """  
      self.DealerWarrantyExpiration:str = obj["DealerWarrantyExpiration"]
      """  Dealer specifc warranty expiration date.  """  
      self.DealerWarrantyStart:str = obj["DealerWarrantyStart"]
      """  Dealer specific warranty start date.  """  
      self.OriginalSerialNum:str = obj["OriginalSerialNum"]
      """  Original Serial Number  """  
      self.OriginalPartNum:str = obj["OriginalPartNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID of Location Inventory  """  
      self.LocationSeqNum:int = obj["LocationSeqNum"]
      """  LocationSeqNum  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer the transfer is for at that time.  """  
      self.CustShipToNum:str = obj["CustShipToNum"]
      """  The current ship to the transfer is for at that time.  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the address for given location type at that time.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the address for given location type at that time.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the address for given location type at that time.  """  
      self.City:str = obj["City"]
      """  City portion of the address for given location type at that time.  """  
      self.Contact:str = obj["Contact"]
      """  Contact Name for given location type at that time.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country number for the Ship To location for at that time.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  The email address for given location type at that time.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax number for given location type at that time.  """  
      self.Name:str = obj["Name"]
      """  Name for for given location type at that time.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone number for for given location type at that time  """  
      self.State:str = obj["State"]
      """  The state or province portion to the location for at that time.  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion to location for at that time.  """  
      self.WarrantyTransfer:str = obj["WarrantyTransfer"]
      """  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  This columns is nno longer used.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date when transfer occurred  """  
      self.Comment:str = obj["Comment"]
      """  Comment about the transfer transaction.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty Code  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty Comment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  Date when the warranty started.  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Date when the warranty expires.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerECCType:str = obj["CustomerECCType"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationWarrantyTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  LocationNum  """  
      self.WarrantySeqNum:int = obj["WarrantySeqNum"]
      """  Sequence number.  This is system generated and is not maintainable.  """  
      self.IDNum:str = obj["IDNum"]
      """  Finished good Identificaton Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  SerialNum  """  
      self.Comment:str = obj["Comment"]
      """  Comment about the warranty transfer transaction.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Effective Date  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  HDCaseNum  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  ParentPartNum  """  
      self.OriginalPartNum:str = obj["OriginalPartNum"]
      """  OriginalPartNum  """  
      self.OriginalPartSerialNum:str = obj["OriginalPartSerialNum"]
      """  OriginalPartSerialNum  """  
      self.NewPartNum:str = obj["NewPartNum"]
      """  NewPartNum  """  
      self.NewPartSerialNum:str = obj["NewPartSerialNum"]
      """  NewPartSerialNum  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  WarrantyCode  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  WarrantyComment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  Date when warranty started.  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Date when warranty expires  """  
      self.DealerWarranty:str = obj["DealerWarranty"]
      """  Dealer Warranty, this is for a non Erp warranty.  """  
      self.DealerWarrantyDesc:str = obj["DealerWarrantyDesc"]
      """  Dealer warranty description, this is for a non Erp warranty  """  
      self.DealerWarrantyStart:str = obj["DealerWarrantyStart"]
      """  Date dealer warranty started, this is for a non Erp warranty  """  
      self.DealerWarrantyExpiration:str = obj["DealerWarrantyExpiration"]
      """  Date dealer warranty expires, this is for a non Erp warranty.  """  
      self.WarrantyUsage:str = obj["WarrantyUsage"]
      """  WarrantyUsage  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum  """  
      self.SystemCreated:bool = obj["SystemCreated"]
      """  SystemCreated  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangedLocationWarrantyTranPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class ChangedLocationWarrantyTranPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class ChangedPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedWarrantyCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class ChangedWarrantyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   locationNum
   """  
   def __init__(self, obj):
      self.locationNum:int = obj["locationNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_LocationInventoryAddressRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID of parent location  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  """  
      self.CustNum:int = obj["CustNum"]
      """  Unique customer number for this location.  """  
      self.CustShipToNum:str = obj["CustShipToNum"]
      """  Ship To number for this locatoin  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the address for this location.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the address for this location.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the address for this location.  """  
      self.City:str = obj["City"]
      """  City portion of the address for this location  """  
      self.Contact:str = obj["Contact"]
      """  Contact for this location.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country Number for this location.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  The email address for this location.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax number for this location  """  
      self.Name:str = obj["Name"]
      """  Name for this location.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone number for this location.  """  
      self.State:str = obj["State"]
      """  State for this location.  """  
      self.Zip:str = obj["Zip"]
      """  Zip for this locatoin  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Use OTS  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ConNum:int = obj["ConNum"]
      """  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  """  
      self.TranComment:str = obj["TranComment"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.CustomerECCType:str = obj["CustomerECCType"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventoryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID for Location Inventory record  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of part.  """  
      self.IDNum:str = obj["IDNum"]
      """  Identification Number (example HIN, VIN).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventoryListTableset:
   def __init__(self, obj):
      self.LocationInventoryList:list[Erp_Tablesets_LocationInventoryListRow] = obj["LocationInventoryList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LocationInventoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID for Location Inventory record  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation.  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The sales order number that this detail shipment line is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this shipment detail line is linked to.  M  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that supplied the quantity that was shipped.  """  
      self.CurrentOwner:str = obj["CurrentOwner"]
      """  This is the current owner.  Valid values are (D)istributor, (C)ustomer  """  
      self.OrderComment:str = obj["OrderComment"]
      """  Order Comment  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.Listing:str = obj["Listing"]
      """  The type of listing the location inventory item is: L=Leaser, S=Sale  """  
      self.ListingStartDate:str = obj["ListingStartDate"]
      """  Date when the location inventory was listed.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty Comment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  Date the warrany started.  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Date the warranty will expired.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Num  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of part.  """  
      self.IDNum:str = obj["IDNum"]
      """  Identification Number (example HIN, VIN).  """  
      self.WarrantyTransfer:str = obj["WarrantyTransfer"]
      """  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.InventoryAttributeSetID:int = obj["InventoryAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AddrList:str = obj["AddrList"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.ExtAddress1:str = obj["ExtAddress1"]
      self.ExtAddress2:str = obj["ExtAddress2"]
      self.ExtAddress3:str = obj["ExtAddress3"]
      self.ExtCity:str = obj["ExtCity"]
      self.ExtContact:str = obj["ExtContact"]
      self.ExtCountryNum:int = obj["ExtCountryNum"]
      self.ExtEmailAddress:str = obj["ExtEmailAddress"]
      self.ExtFaxNum:str = obj["ExtFaxNum"]
      self.ExtName:str = obj["ExtName"]
      self.ExtPhoneNum:str = obj["ExtPhoneNum"]
      self.ExtState:str = obj["ExtState"]
      self.ExtZIP:str = obj["ExtZIP"]
      self.NewAddrList:str = obj["NewAddrList"]
      self.NewCustID:str = obj["NewCustID"]
      self.NewCustNum:int = obj["NewCustNum"]
      self.NewShipToNum:str = obj["NewShipToNum"]
      self.NewUseOTMF:bool = obj["NewUseOTMF"]
      self.TrackIDNum:bool = obj["TrackIDNum"]
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      self.TranComment:str = obj["TranComment"]
      """  Transaction Comment  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Use OTS  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.SoldToAddrList:str = obj["SoldToAddrList"]
      """  Sold to address  """  
      self.OwnerAddrList:str = obj["OwnerAddrList"]
      """  Owner address.  """  
      self.LocationAddrList:str = obj["LocationAddrList"]
      """  Location Address.  """  
      self.TransferAddrType:str = obj["TransferAddrType"]
      """  Where is the transfer going to: (N)o Address Change,  (L)ocation, (O)wner, (B)oth.  Blank will be for a warranty change only.  """  
      self.OwnerBusinessModel:str = obj["OwnerBusinessModel"]
      """  Owner Busines Model  """  
      self.LocationBusinessModel:str = obj["LocationBusinessModel"]
      """  Location Business Model  """  
      self.OwnerCustID:str = obj["OwnerCustID"]
      """  Owner Customer ID  """  
      self.OwnerShipToNum:str = obj["OwnerShipToNum"]
      """  Owner Ship To.  """  
      self.OwnerUseOTMF:bool = obj["OwnerUseOTMF"]
      """  Owner Use One Time Mark For.  """  
      self.LocationCustID:str = obj["LocationCustID"]
      """  Location Customer ID.  """  
      self.LocationShipToNum:str = obj["LocationShipToNum"]
      """  Location Ship To.  """  
      self.LocationUseOTMF:bool = obj["LocationUseOTMF"]
      """  Location Use One Time Mark For.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  Sold To Customer ID.  """  
      self.SoldToShipToNum:str = obj["SoldToShipToNum"]
      """  Sold To Ship To.  """  
      self.SoldToUseOTMF:bool = obj["SoldToUseOTMF"]
      """  Sold To Use Ont Time Mark For.  """  
      self.SoldToBusinessModel:str = obj["SoldToBusinessModel"]
      """  Sold To Business Model  """  
      self.OwnerAddrType:str = obj["OwnerAddrType"]
      """  Addres type of owner : L=Locatoin, O=Owner, S=Sold To  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date when transfer occured - writes to LocationTran.EffectiveDate  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      self.NewConNum:int = obj["NewConNum"]
      """  Establishes the contact to be used for the Location Inventory Address records. The contact will be specific for the address type (Lease, Owner, Sold To).  Contains the key value for the contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table.  """  
      self.LocationAttn:str = obj["LocationAttn"]
      """  External field to hold the name of the selected customer contact for the Location record  """  
      self.NewConName:str = obj["NewConName"]
      """  External field to hold the name of the selected customer contact for the selected record  """  
      self.OwnerAttn:str = obj["OwnerAttn"]
      """  External field to hold the name of the selected customer contact for the Owner record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationInventoryTableset:
   def __init__(self, obj):
      self.LocationInventory:list[Erp_Tablesets_LocationInventoryRow] = obj["LocationInventory"]
      self.LocationInventoryAddress:list[Erp_Tablesets_LocationInventoryAddressRow] = obj["LocationInventoryAddress"]
      self.LocationMtl:list[Erp_Tablesets_LocationMtlRow] = obj["LocationMtl"]
      self.LocationTran:list[Erp_Tablesets_LocationTranRow] = obj["LocationTran"]
      self.LocationWarrantyTran:list[Erp_Tablesets_LocationWarrantyTranRow] = obj["LocationWarrantyTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LocationMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  """  
      self.Description:str = obj["Description"]
      """  A description of the material.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent.  Field Service was EstQty in FSCallMt.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  The unit used to measure the material.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.  When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """  A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.  It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material.  Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Job Material.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      """  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  """  
      self.SalvageCredit:int = obj["SalvageCredit"]
      """  Total salvage credit to date.  A summary of salvage receipt transactions.  """  
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      """  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  """  
      self.Ordered:bool = obj["Ordered"]
      """  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  """  
      self.PurComment:str = obj["PurComment"]
      """  Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  Indicates if this material will be backflushed.  Note: this field is defaulted from Part.BackFlush Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobMtl is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      """  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      """  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      """  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      """  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """  Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler: 'I' to ignore in eScheduler.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this Material belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this material relates to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the Material in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the Material in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the material in customers currency.  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.Billable:bool = obj["Billable"]
      """  Is this a billable material item.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Holds the quantity of the item that has been shipped through misc.  shipments  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the Material in Customer currency.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  """  
      self.AddedMtl:bool = obj["AddedMtl"]
      """  This material was added after initial setup of the job  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.SCMiscCode:str = obj["SCMiscCode"]
      """  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """  RFQ SRFQ Status: W= Waiting, A = Accepted, R = Requested, C = Receivedtatus.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.WIReqDate:str = obj["WIReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      """  Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """  Unit of Measure of the JobMtl.BaseRequiredQty.  If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  """  
      self.PickError:str = obj["PickError"]
      """  A non blank character indicates that the release could not be picked by the Auto Pick process. The possible values are: "L" - Order Line can't be shipped complete. "O" - Order can't be shipped complete. "I" - Insufficient quantity reserved"Z" - Zero quantity reserved.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """  Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """  Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """  Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where: EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      """  Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      """  Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      """  Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      """  Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where: SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.LoanedQty:int = obj["LoanedQty"]
      """  The material quantity that has been loaned out to another job.  """  
      self.BorrowedQty:int = obj["BorrowedQty"]
      """  The material quantity that has been borrowed from another job.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      """  IsPOCostingMaintained  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.POCostingFactor:int = obj["POCostingFactor"]
      """  POCostingFactor  """  
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      """  PlannedQtyPerUnit  """  
      self.POCostingDirection:int = obj["POCostingDirection"]
      """  POCostingDirection  """  
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      """  POCostingUnitVal  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.ContractID:str = obj["ContractID"]
      """  Contract ID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.StagingLotNum:str = obj["StagingLotNum"]
      """  Stores the lot number of the material in the Staging Warehouse/Bin.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum  """  
      self.SerialNum:str = obj["SerialNum"]
      """  SerialNum  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  WarrantyCode  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  WarrantyComment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  WarrantyStartDate  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  WarrantyExpirationDate  """  
      self.LocationNum:int = obj["LocationNum"]
      """  LocationNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.DealerWarranty:str = obj["DealerWarranty"]
      """  Dealer specific warranty code.  This is a non ERP warranty code.  """  
      self.DealerWarrantyDesc:str = obj["DealerWarrantyDesc"]
      """  Dealer specific warranty description  """  
      self.DealerWarrantyExpiration:str = obj["DealerWarrantyExpiration"]
      """  Dealer specifc warranty expiration date.  """  
      self.DealerWarrantyStart:str = obj["DealerWarrantyStart"]
      """  Dealer specific warranty start date.  """  
      self.OriginalSerialNum:str = obj["OriginalSerialNum"]
      """  Original Serial Number  """  
      self.OriginalPartNum:str = obj["OriginalPartNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID of Location Inventory  """  
      self.LocationSeqNum:int = obj["LocationSeqNum"]
      """  LocationSeqNum  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer the transfer is for at that time.  """  
      self.CustShipToNum:str = obj["CustShipToNum"]
      """  The current ship to the transfer is for at that time.  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address this transaction is related to: L=Lease, O=Owner, S=Sold To.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the address for given location type at that time.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the address for given location type at that time.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the address for given location type at that time.  """  
      self.City:str = obj["City"]
      """  City portion of the address for given location type at that time.  """  
      self.Contact:str = obj["Contact"]
      """  Contact Name for given location type at that time.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country number for the Ship To location for at that time.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  The email address for given location type at that time.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax number for given location type at that time.  """  
      self.Name:str = obj["Name"]
      """  Name for for given location type at that time.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Phone number for for given location type at that time  """  
      self.State:str = obj["State"]
      """  The state or province portion to the location for at that time.  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion to location for at that time.  """  
      self.WarrantyTransfer:str = obj["WarrantyTransfer"]
      """  What kind of warranty transfer this is: (F)ull/(L)imited/(N)o  This columns is nno longer used.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date when transfer occurred  """  
      self.Comment:str = obj["Comment"]
      """  Comment about the transfer transaction.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty Code  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Warranty Comment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  Date when the warranty started.  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Date when the warranty expires.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerECCType:str = obj["CustomerECCType"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationWarrantyTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  LocationNum  """  
      self.WarrantySeqNum:int = obj["WarrantySeqNum"]
      """  Sequence number.  This is system generated and is not maintainable.  """  
      self.IDNum:str = obj["IDNum"]
      """  Finished good Identificaton Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  SerialNum  """  
      self.Comment:str = obj["Comment"]
      """  Comment about the warranty transfer transaction.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Effective Date  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  HDCaseNum  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  ParentPartNum  """  
      self.OriginalPartNum:str = obj["OriginalPartNum"]
      """  OriginalPartNum  """  
      self.OriginalPartSerialNum:str = obj["OriginalPartSerialNum"]
      """  OriginalPartSerialNum  """  
      self.NewPartNum:str = obj["NewPartNum"]
      """  NewPartNum  """  
      self.NewPartSerialNum:str = obj["NewPartSerialNum"]
      """  NewPartSerialNum  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  WarrantyCode  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  WarrantyComment  """  
      self.WarrantyStartDate:str = obj["WarrantyStartDate"]
      """  Date when warranty started.  """  
      self.WarrantyExpirationDate:str = obj["WarrantyExpirationDate"]
      """  Date when warranty expires  """  
      self.DealerWarranty:str = obj["DealerWarranty"]
      """  Dealer Warranty, this is for a non Erp warranty.  """  
      self.DealerWarrantyDesc:str = obj["DealerWarrantyDesc"]
      """  Dealer warranty description, this is for a non Erp warranty  """  
      self.DealerWarrantyStart:str = obj["DealerWarrantyStart"]
      """  Date dealer warranty started, this is for a non Erp warranty  """  
      self.DealerWarrantyExpiration:str = obj["DealerWarrantyExpiration"]
      """  Date dealer warranty expires, this is for a non Erp warranty.  """  
      self.WarrantyUsage:str = obj["WarrantyUsage"]
      """  WarrantyUsage  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum  """  
      self.SystemCreated:bool = obj["SystemCreated"]
      """  SystemCreated  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FSWarrCdWarrDescription:str = obj["FSWarrCdWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LocationWarrantyTranTableset:
   def __init__(self, obj):
      self.LocationWarrantyTran:list[Erp_Tablesets_LocationWarrantyTranRow] = obj["LocationWarrantyTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtLocationInventoryTableset:
   def __init__(self, obj):
      self.LocationInventory:list[Erp_Tablesets_LocationInventoryRow] = obj["LocationInventory"]
      self.LocationInventoryAddress:list[Erp_Tablesets_LocationInventoryAddressRow] = obj["LocationInventoryAddress"]
      self.LocationMtl:list[Erp_Tablesets_LocationMtlRow] = obj["LocationMtl"]
      self.LocationTran:list[Erp_Tablesets_LocationTranRow] = obj["LocationTran"]
      self.LocationWarrantyTran:list[Erp_Tablesets_LocationWarrantyTranRow] = obj["LocationWarrantyTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   locationNum
   """  
   def __init__(self, obj):
      self.locationNum:int = obj["locationNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LocationInventoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LocationInventoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LocationInventoryTableset] = obj["returnObj"]
      pass

class GetCurrentAddress_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class GetCurrentAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_LocationInventoryListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLocationWarrantyTran_input:
   """ Required : 
   locationNum
   idNum
   """  
   def __init__(self, obj):
      self.locationNum:int = obj["locationNum"]
      self.idNum:str = obj["idNum"]
      pass

class GetLocationWarrantyTran_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LocationWarrantyTranTableset] = obj["returnObj"]
      pass

class GetNewCustomerAddress_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class GetNewCustomerAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLocationInventoryAddress_input:
   """ Required : 
   ds
   locationNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      self.locationNum:int = obj["locationNum"]
      pass

class GetNewLocationInventoryAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLocationInventory_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class GetNewLocationInventory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLocationMtl_input:
   """ Required : 
   ds
   locationNum
   jobNum
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      self.locationNum:int = obj["locationNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewLocationMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLocationTran_input:
   """ Required : 
   ds
   locationNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      self.locationNum:int = obj["locationNum"]
      pass

class GetNewLocationTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLocationWarrantyTran_input:
   """ Required : 
   ds
   locationNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      self.locationNum:int = obj["locationNum"]
      pass

class GetNewLocationWarrantyTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOTMFAddress_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class GetNewOTMFAddress_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLocationInventory
   whereClauseLocationInventoryAddress
   whereClauseLocationMtl
   whereClauseLocationTran
   whereClauseLocationWarrantyTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLocationInventory:str = obj["whereClauseLocationInventory"]
      self.whereClauseLocationInventoryAddress:str = obj["whereClauseLocationInventoryAddress"]
      self.whereClauseLocationMtl:str = obj["whereClauseLocationMtl"]
      self.whereClauseLocationTran:str = obj["whereClauseLocationTran"]
      self.whereClauseLocationWarrantyTran:str = obj["whereClauseLocationWarrantyTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LocationInventoryTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtLocationInventoryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLocationInventoryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LocationInventoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCustomer_input:
   """ Required : 
   proposedCustID
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      pass

class ValidateCustomer_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class ValidateIDNumber_input:
   """ Required : 
   partNum
   proposeIDNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.proposeIDNum:str = obj["proposeIDNum"]
      pass

class ValidateIDNumber_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateMaterialLotNumber_input:
   """ Required : 
   partNum
   jobNum
   proposeLotNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.jobNum:str = obj["jobNum"]
      self.proposeLotNum:str = obj["proposeLotNum"]
      pass

class ValidateMaterialLotNumber_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateMaterialOrigSerialNumber_input:
   """ Required : 
   partNum
   jobNum
   proposeSerialNo
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.jobNum:str = obj["jobNum"]
      self.proposeSerialNo:str = obj["proposeSerialNo"]
      pass

class ValidateMaterialOrigSerialNumber_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidatePartNum_input:
   """ Required : 
   proposedPartNum
   """  
   def __init__(self, obj):
      self.proposedPartNum:str = obj["proposedPartNum"]
      pass

class ValidatePartNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateSerialNumber_input:
   """ Required : 
   partNum
   proposeSerialNo
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.proposeSerialNo:str = obj["proposeSerialNo"]
      pass

class ValidateSerialNumber_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateShipTo_input:
   """ Required : 
   custNum
   proposedShipTo
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.proposedShipTo:str = obj["proposedShipTo"]
      pass

class ValidateShipTo_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

